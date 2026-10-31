class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        norm_email = set()

        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")

            norm_email.add(local + "@" + domain)

        return len(norm_email)


emails = ["test.email+alex@neetcode.com","test.e.mail+bob.cathy@neetcode.com","testemail+david@nee.tcode.com"]
print(Solution().numUniqueEmails(emails))