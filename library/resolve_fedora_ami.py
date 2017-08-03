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
        ('eu-central-1', True): 'ami-9a65c5f5',
        ('us-east-1', True): 'ami-1f595c09',
        ('us-west-1', True): 'ami-a8103fc8',
        ('us-west-2', True): 'ami-96180bef',
        ('eu-central-1', False): 'ami-5364c43c',
        ('us-east-1', False): 'ami-bb6065ad',
        ('us-west-1', False): 'ami-31113e51',
        ('us-west-2', False): 'ami-2c1c0f55',
    }

    module.exit_json(changed=False, name=images.get((region, ssd), ''))


if __name__ == '__main__':
    main()