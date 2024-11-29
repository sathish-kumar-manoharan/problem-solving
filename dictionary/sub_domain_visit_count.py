from typing import List
"""
https://leetcode.com/problems/subdomain-visit-count/

Let n be the number of domain strings in the input array cpdomains, and m be the maximum number of fragments in any domain.
Time: O(N * M)
Space: O(N * M)
"""

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        lookup = {}

        for domain in cpdomains:
            split = domain.split(" ")
            visit = int(split[0])

            sub_domain_list = split[1].split(".")

            for index in range(len(sub_domain_list)):
                sub_domain = ".".join(sub_domain_list[index:])
                
                lookup[sub_domain] = lookup.get(sub_domain, 0) + visit

        result = []

        for key, value in lookup.items():
            result.append(f"{value} {key}")

        return result