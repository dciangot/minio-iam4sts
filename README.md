# Quick start

- Rertrieve an access token from the `iam-demo.cloud.cnaf.infn.it` and set it in the `TOKEN` env var
- `pip3 install --user -r requirements.txt`
- `curl https://rclone.org/install.sh | sudo bash`
- `TOKEN=$TOKEN python3 main.py`
    - this will use the id_token provided retrieve minio credentials
    - check if the user bucket exists and create it if not
    - mount all the user buckets in /tmp/<username>
    - do some operation
    - unmount the volume and exit