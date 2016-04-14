# Copyright (C) 2010-2013 Claudio Guarnieri.
# Copyright (C) 2014-2016 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from cuckoo.misc import cwd

domains = set()

def is_whitelisted_domain(domain):
    return domain in domains

# Initialize the domain whitelist.
for domain in open(cwd("whitelist", "domain.txt")):
    domains.add(domain.strip())