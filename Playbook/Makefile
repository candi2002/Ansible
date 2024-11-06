# Makefile to automate Git operations

# Variables
REPO_URL = git@github.com:candi2002/Ansible.git
DEST_DIR = /opt/ansible/demo

# Default target
all: help

# Help target
help:
	@echo "Usage:"
	@echo "  make clone   - Clone the repository"
	@echo "  make pull    - Pull the latest changes"
	@echo "  make push    - Push local changes"

# Clone target
clone:
	@if [ ! -d "$(DEST_DIR)/.git" ]; then \
		git clone $(REPO_URL) $(DEST_DIR); \
	else \
		echo "Repository already cloned."; \
	fi

# Pull target
pull:
	@if [ -d "$(DEST_DIR)/.git" ]; then \
		cd $(DEST_DIR) && git pull origin main; \
	else \
		echo "Repository not cloned yet. Run 'make clone' first."; \
	fi

# Push target
push:
	@if [ -d "$(DEST_DIR)/.git" ]; then \
		cd $(DEST_DIR) && git add . && git commit -m "Automated commit" && git push origin main; \
	else \
		echo "Repository not cloned yet. Run 'make clone' first."; \
	fi

