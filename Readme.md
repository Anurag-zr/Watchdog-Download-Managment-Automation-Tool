# Watchdog: Download Management Automation Project

## Introduction
This Python script is designed to monitor a designated folder and automatically organize newly downloaded files based on their extension into corresponding subfolders. It simplifies file management and keeps your download directory organized without manual intervention. The service runs seamlessly in the background, both on macOS and Linux systems, leveraging system-native schedulers like launchd and systemd to ensure reliability and minimal performance impact.

## Features
- Watches for files in a specified directory.
- Automatically moves files to folders based on file extension.
- Runs continuously as a background service on both macOS and Linux.

## Running the Script as a Service

### On macOS
To run this script as a service on macOS, you will use `launchd` to create a Launch Agent. Here's how you can set it up:

1. **Create a Launch Agent plist file**: Create a file named `com.yourusername.downloadautomation.plist` in `~/Library/LaunchAgents/`.
2. **Edit the plist file** to run the script at login:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.yourusername.downloadautomation</string>
       <key>ProgramArguments</key>
       <array>
           <string>/usr/local/bin/python3</string>
           <string>/path/to/your/script.py</string>
       </array>
       <key>KeepAlive</key>
       <true/>
       <key>RunAtLoad</key>
       <true/>
   </dict>
   </plist>

### On linux
To run this script as a service on linux, you will use systemd service in linux. Here's how you can set it up:

1. **Create a systemd service file**: Save the following to /etc/systemd/system/downloadautomation.service:
 ```ini
[Unit]
Description=Download Automation Service
After=network.target

[Service]
Type=simple
User=username
ExecStart=/usr/bin/python3 /path/to/your/script.py
Restart=on-failure

[Install]
WantedBy=multi-user.target

```bash
sudo systemctl enable downloadautomation.service
sudo systemctl start downloadautomation.service

