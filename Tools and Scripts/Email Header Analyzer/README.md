# Email Header Analyzer

## Overview

Email Header Analyzer is a powerful Python tool designed to parse and analyze email headers. It extracts crucial information from email headers, including sender details, recipient information, routing data, and performs geolocation lookups on IP addresses found in the headers. This tool is invaluable for email forensics, security analysis, OSINT and understanding the journey of an email from sender to recipient.

## Features

- Parse email headers from a file
- Extract key information such as From, To, Subject, Date, Message-ID, etc.
- Identify and extract IP addresses from Received headers
- Perform geolocation lookups on extracted IP addresses
- Display detailed information about each IP, including country, city, ISP, and more

## Why It's Needed

Email headers contain a wealth of information that is often overlooked. This tool helps in:

1. Identifying potential phishing or spam emails
2. Tracing the path of an email
3. Verifying the authenticity of an email
4. Investigating email-related security incidents


## Necessary Dependencies

Run following command to install necessary dependencies
```
pip3 install beautifulsoup4 requests
```
- If not using Python 3, then change pip3 --> pip


## Usage

Run the script from the command line, providing the path to your email header file:

```
python email_header_analyzer.py -f path/to/your/email_header.txt

or

python3 email_header_analyzer.py -f path/to/your/email_header.txt

//depending on your system and python version
```

## Sample Output

```
Email Information:
From: sender@example.com
To: recipient@example.com
Subject: Important Message
Date: Mon, 1 Jan 2023 12:00:00 +0000
Message-ID: <abc123@mail.example.com>
...

Extracted IP Addresses:
  IP: 192.0.2.1
    Location: United States, California, San Francisco
    Postal Code: 94105
    ISP: Example ISP
    Organization: Example Org
    Coordinates: 37.7749, -122.4194
...
```

## Future Enhancements

This tool provides a solid foundation for email header analysis. Future enhancements could include:

1. Development of a browser plugin for quick analysis of email headers directly from the email client.
2. Integration with local email databases for automated scanning and flagging of suspicious emails.
3. Creation of a graphical user interface for easier interaction and visualization of results.

## Privacy Note

This tool is designed to analyze email headers locally, ensuring that your private email content remains confidential. When using any email analysis tool, always be mindful of privacy concerns and avoid sharing sensitive information.

## Contributing

Contributions to improve and expand this tool are welcome! Please feel free to submit pull requests or open issues to discuss potential enhancements.

## Disclaimer

This tool is provided for educational and informational purposes only. Always respect privacy laws and terms of service when analyzing email headers.
