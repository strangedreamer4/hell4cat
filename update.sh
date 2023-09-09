#!/bin/bash

# Navigate to the installation directory
cd "$INSTALL_DIR"

# Pull updates from the repository (replace with your update process)
git pull origin master

# Display update message
echo "hellcat has been updated."





# Define the repository URL
REPO_URL="https://github.com/strangedreamer4/hellcat.git"
# Define the repository directory
REPO_DIR="hellcat"

# Navigate to the parent directory
cd ..

# Define a function to update the repository
update_repo() {
    if [ -d "$REPO_DIR" ]; then
        if [ -d "$REPO_DIR/.git" ]; then
            echo "Updating repository..."
            cd "$REPO_DIR"
            
            # Stash local changes if any
            git stash
            
            # Pull changes from the remote repository
            git pull origin main
            
            # Apply stashed changes if any
            git stash pop
            
            cd ..
        else
            echo "The '$REPO_DIR' directory exists but is not a Git repository."
            echo "Please manually remove or backup the directory and re-run the script."
        fi
    else
        echo "Cloning repository..."
        git clone "$REPO_URL" "$REPO_DIR"
    fi
}

# Run the update_repo function
update_repo

echo "Update complete!"


