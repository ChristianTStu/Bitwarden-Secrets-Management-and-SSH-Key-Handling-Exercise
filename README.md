# Bitwarden Secrets Management and SSH Key Handling Exercise

Welcome to the Bitwarden Secrets Management and SSH Key Handling Exercise repository. This project is designed to guide you through the process of creating an SSH key pair, managing secrets in Bitwarden, and using a script to access these secrets securely. Below, you'll find detailed steps to help you accomplish each task effectively.

## Overview of Bitwarden and SSH

Bitwarden is a robust secrets management tool that allows you to store and manage sensitive information securely, such as passwords, tokens, and SSH keys. SSH (Secure Shell) keys are a pair of cryptographic keys used to authenticate to an SSH server as an alternative to password-based logins.

## Prerequisites

Ensure that you have administrative privileges on your computer and access to a Virtual Learning Environment (VLE) where you can install software.

## Setup Instructions

1. **Create SSH Key Pair:**
   - Generate a new SSH key pair on your system. This will typically involve using `ssh-keygen` on Unix-like systems or PuTTYgen on Windows.

2. **Install and Configure Bitwarden CLI:**
   - Download the Bitwarden CLI from the [provided link](https://github.com/bitwarden/sdk/releases/download/bws-v0.4.0/bws-x86_64-pc-windows-msvc-0.4.0.zip) and install it on your VLE VM.
   - Follow the detailed instructions on the [Bitwarden CLI documentation page](https://bitwarden.com/help/secrets-manager-cli/#tab-inline-7x4v8ktNB7trBxUx9cFsab) to set up and authenticate the CLI tool.

## Configuration

3. **Create and Manage Secrets Vault:**
   - Set up a secrets vault in Bitwarden where you will store your SSH key and other sensitive information.

4. **Add SSH Key to Bitwarden:**
   - Store your newly created SSH private key as a secret in the Bitwarden vault.

5. **Create Machine Account and Access Token:**
   - Set up a machine account in Bitwarden to facilitate automated access to the secrets vault.
   - Generate an access token for the machine account to authenticate via the Bitwarden CLI without manual login.

6. **Script Creation:**
   - Develop a script using a language of your choice (Python, PowerShell, Bash, etc.) that utilizes the Bitwarden CLI to retrieve your SSH public key from the secrets vault.

## Verification and Submission

7. **Capture and Submit Screenshots and Script:**
   - Take a screenshot showing your SSH key stored in the Bitwarden vault.
   - Capture another screenshot proving the creation of the access token in Bitwarden.
   - Take a screenshot demonstrating that your script can successfully retrieve the SSH key from Bitwarden.
   - Submit the script along with the screenshots as part of your assignment deliverables.

## Support

For assistance with Bitwarden CLI or troubleshooting steps, consult the [Bitwarden Help Center](https://bitwarden.com/help/) or raise an issue in this repository.

Thank you for participating in this exercise to enhance your skills in managing secrets and handling SSH keys using Bitwarden. We look forward to your successful completion of the tasks and your innovative script that interfaces with Bitwarden.
