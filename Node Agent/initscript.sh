#!/bin/bash

# Check if 'wheel' group exists
if getent group wheel > /dev/null 2>&1; then
    GROUP_NAME="wheel"
elif getent group sudo > /dev/null 2>&1; then
    GROUP_NAME="sudo"
else
    echo "Error: Neither 'wheel' nor 'sudo' group exists. Please create one manually."
    exit 1
fi

# Define the username
USERNAME="ai-agent"

# Check if user already exists
if id "$USERNAME" &>/dev/null; then
    echo "User '$USERNAME' already exists."
else
    # Create the user without a password and with no interactive prompts
    sudo useradd -m -s /bin/bash "$USERNAME"
    echo "User '$USERNAME' created successfully."
fi

# Add user to the appropriate group
sudo usermod -aG "$GROUP_NAME" "$USERNAME"
echo "User '$USERNAME' added to '$GROUP_NAME' group."

# Verify the user's sudo access
echo "Verifying user access:"
su - "$USERNAME" -c "groups"

echo "Setup completed successfully!"
