class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []

        for email in emails:
            s = email.split("@")
            em = ""
            for l in s[0]:
                if l == "+":
                    em += s[1]
                    break
                elif l.isalnum():
                    em += l

            print(em)
            res.append(em)    
        return len(set(res))    