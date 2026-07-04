#!/usr/bin/env python3

import re
import csv


def contains_domain(address, domain):
    """Returns True if the email address contains the given domain."""
    domain_pattern = r'[\w\.-]+@' + re.escape(domain) + r'$'
    return re.match(domain_pattern, address) is not None


def replace_domain(address, old_domain, new_domain):
    """Replaces the old domain with the new domain."""
    old_domain_pattern = re.escape(old_domain) + r'$'
    return re.sub(old_domain_pattern, new_domain, address)


def main():
    old_domain = "abc.edu"
    new_domain = "xyz.edu"

    # Files in the current directory
    csv_file_location = "user_emails.csv"
    report_file = "updated_user_emails.csv"

    # Read CSV
    with open(csv_file_location, "r", newline="") as file:
        user_data_list = list(csv.reader(file))

    # Find the Email Address column
    email_index = user_data_list[0].index(" Email Address")

    # Update email addresses
    for user in user_data_list[1:]:
        email = user[email_index].strip()
        if contains_domain(email, old_domain):
            user[email_index] = replace_domain(email, old_domain, new_domain)

    # Write updated CSV
    with open(report_file, "w", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)

    print(f"Updated file created: {report_file}")


if __name__ == "__main__":
    main()
