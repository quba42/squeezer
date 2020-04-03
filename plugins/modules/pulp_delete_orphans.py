#!/usr/bin/python
# -*- coding: utf-8 -*-

# copyright (c) 2019, Matthias Dellweg
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}


DOCUMENTATION = r'''
---
module: pulp_delete_orphans
short_description: Deletes all orphaned entities of a pulp server
description:
  - "This module deletes all orphaned artifacts and content units of a pulp server."
options: {}
extends_documentation_fragment:
  - mdellweg.squeezer.pulp
author:
  - Matthias Dellweg (@mdellweg)
'''

EXAMPLES = r'''
- name: Delete orphans
  pulp_delete_orphans:
    api_url: localhost:24817
    username: admin
    password: password
'''

RETURN = r'''
  summary:
    description: Summary of deleted entities
    type: dict
    returned: always
'''


from ansible_collections.mdellweg.squeezer.plugins.module_utils.pulp_helper import (
    PulpAnsibleModule,
    PulpOrphans,
)


def main():
    with PulpAnsibleModule() as module:
        summary = PulpOrphans(module).delete()
        module.set_result('summary', summary)


if __name__ == '__main__':
    main()
