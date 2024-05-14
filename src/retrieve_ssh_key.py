import subprocess
import json

# Function to run Bitwarden CLI command and return JSON output
def run_bws_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return json.loads(output.decode())

# Function to get SSH key from Bitwarden vault
def get_ssh_key(access_token, item_id):
    # Get SSH key item
    ssh_key_item = run_bws_command(f'bws secret get {item_id} --access-token {access_token}')
    ssh_key = ssh_key_item
    
    return ssh_key

# Main function
def main():
    # Your access token obtained from Bitwarden
    access_token = "0.452798fc-f524-4d91-a476-b1660158e177.T8kU5DtqE8vELtzpfFMH2x9WKo2ssd:zuEOq1XnqlikOiU7iRcEeg=="
    
    # The ID of the SSH key item in your Bitwarden vault
    item_id = "22c43dfe-ea7e-4a78-a357-b1660156bf32"

    # Get SSH key
    ssh_key = get_ssh_key(access_token, item_id)
    print("SSH Public Key:")
    print(ssh_key)

if __name__ == "__main__":
    main()

