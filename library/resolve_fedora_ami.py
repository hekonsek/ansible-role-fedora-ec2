#!/usr/bin/python

from ansible.module_utils.basic import *

def main():

    module = AnsibleModule(
        argument_spec = dict(
            region = dict(required=True),
            ssd = dict(required=True)
        )
    )

    region = module.params['region']
    ssd = bool(module.params['ssd'])

    images = {
        ('us-east-1', True): 'ami-8afb4df0',
        ('us-west-1', True): 'ami-4ec7f82e	',
        ('us-west-2', True): 'ami-959441ed',
        ('eu-west-1', True): 'ami-2334975a',
        ('eu-central-1', True): 'ami-d371f5bc',
        ('us-east-1', False): 'ami-bcf84ec6',
        ('us-west-1', False): 'ami-18c7f878',
        ('us-west-2', False): 'ami-3594414d',
        ('eu-central-1', False): 'ami-5f7cf830',
    }

    module.exit_json(changed=False, name=images.get((region, ssd), ''))


if __name__ == '__main__':
    main()