import re

# Suspicious Patterns

PHISHING_KEYWORDS = [
    'urgent','immediate', 'action required', 'verify your account',
    'login to your account', 'suspended', 'unusual activity', 
    'click here', 'reset your password'
]

SUSPICIOUS_URL_PATTERNS = r'https?"//[^\s]+'
SENDER_MISMATCH_PATTERNS = [
    r'from:\s*([^\n]+)',
    r'reply-to:\s*([^\n]+)'
]

def load_email(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def find_phishing_keywords(email_content):
    found = []
    for word in PHISHING_KEYWORDS:
        if re.search(rf'\b{re.escape(word)}\b', email_content, re.IGNORECASE):
            found.append(word)
    return found

def find_urls(email_content):
    return re.findall(SUSPICIOUS_URL_PATTERNS, email_content)

def detect_sender_mismatch(email_content):
    senders = []
    for pattern in SENDER_MISMATCH_PATTERNS:
        match = re.search(pattern, email_content, re.IGNORECASE)
        if match:
            senders.append(match.group(1).strip())
    if len(senders) == 2 and senders[0] != senders[1]:
        return senders
    return None

def email_phishing_report(file_path):
    email = load_email(file_path)
    print(f"\n--- Phishing Scan Report for: {file_path} ---\n")
    keywords = find_phishing_keywords(email)
    if keywords:
        print(f"Phishing keywords detected: {keywords}")
    else:
        print("No typical phishing keywords found.")

    urls = find_urls(email)
    print(f"Suspicious URLs found: {urls if urls else 'None'}")

    mismatch = detect_sender_mismatch(email)
    if mismatch:
        print(f"Sender mismatch detected: {mismatch}")
    else:
        print("No sender mismatch found.")
    print("\nScan Complete.")

# Command-line usage 
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python phishing_detector.py <email_file.txt>")
    else:
        email_phishing_report(sys.argv[1])
