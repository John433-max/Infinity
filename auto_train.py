
import os
import time
import subprocess
from train_model import train_model

def commit_and_push_changes():
    # Add changes to git
    subprocess.run(['git', 'add', '.'])
    
    # Commit changes
    subprocess.run(['git', 'commit', '-m', 'Auto-trained model update'])
    
    # Push changes to GitHub
    token = os.getenv('GITHUB_TOKEN')
    subprocess.run(['git', 'push', f'https://{token}@github.com/John433-max/Infinity.git'])

def auto_train():
    while True:
        # Train the model
        train_model()
        
        # Commit and push changes to GitHub
        commit_and_push_changes()
        
        # Wait for a specified period before retraining (e.g., 24 hours)
        time.sleep(86400)

if __name__ == '__main__':
    auto_train()
