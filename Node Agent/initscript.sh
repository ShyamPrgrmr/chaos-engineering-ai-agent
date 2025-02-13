#!/bin/bash

USERNAME="ai-agent"
SSH_DIR="/home/$USERNAME/.ssh"
AUTHORIZED_KEYS="$SSH_DIR/authorized_keys"
KEY_DIR="/root"
PEM_FILE="$KEY_DIR/$USERNAME.pem"

# Check for sudo or wheel group
if getent group wheel > /dev/null 2>&1; then
    GROUP_NAME="wheel"
elif getent group sudo > /dev/null 2>&1; then
    GROUP_NAME="sudo"
else
    echo "Error: Neither 'wheel' nor 'sudo' group exists. Please create one manually."
    exit 1
fi

# Create the user if it does not exist
if ! id "$USERNAME" &>/dev/null; then
    echo "Creating user '$USERNAME'..."
    sudo useradd -m -s /bin/bash "$USERNAME"
    echo "User '$USERNAME' created successfully."
else
    echo "User '$USERNAME' already exists."
fi

# Add the user to the appropriate group
sudo usermod -aG "$GROUP_NAME" "$USERNAME"
echo "User '$USERNAME' added to '$GROUP_NAME' group."

# Create SSH directory if it doesn’t exist
if [ ! -d "$SSH_DIR" ]; then
    echo "Creating SSH directory..."
    sudo mkdir -p "$SSH_DIR"
    sudo chown "$USERNAME:$USERNAME" "$SSH_DIR"
    sudo chmod 700 "$SSH_DIR"
fi

# Generate SSH key pair if not already present
if [ ! -f "$PEM_FILE" ]; then
    echo "Generating SSH key pair..."
    sudo ssh-keygen -t rsa -b 4096 -m PEM -f "$PEM_FILE" -q -N ""
    sudo chmod 400 "$PEM_FILE"
    sudo chown root:root "$PEM_FILE"
    echo "SSH key pair generated at: $PEM_FILE"
else
    echo "SSH key already exists at: $PEM_FILE"
fi

# Add public key to authorized_keys
PUB_KEY="${PEM_FILE}.pub"
if [ -f "$PUB_KEY" ]; then
    echo "Setting up SSH access..."
    sudo cp "$PUB_KEY" "$AUTHORIZED_KEYS"
    sudo chmod 600 "$AUTHORIZED_KEYS"
    sudo chown "$USERNAME:$USERNAME" "$AUTHORIZED_KEYS"
else
    echo "Error: Public key file not found!"
    exit 1
fi

# Configure SSH to disable password authentication and allow key-based login
echo "Configuring SSH for key-based authentication..."
sudo sed -i 's/^#\?PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo sed -i 's/^#\?PubkeyAuthentication no/PubkeyAuthentication yes/' /etc/ssh/sshd_config
sudo systemctl restart sshd

# Output the .pem file location
echo "Passwordless SSH setup completed!"


