# Ansible Role - Fedora EC2 instance

Provisions Fedora 26 on AWS EC2. It ensures that:
- Fedora 26 AWS EC2 node is provisioned and started
- public SSH key is uploaded and assigned to provisioned EC2 node
- EC2 security group firewall has been configured to accept only SSH traffic
- OpenSSH server is up and running
- Ansible-friendly version of Python is installed on provisioned instance

## Compatibility

This playbook has been tested against Fedora 26.

## Requirements

Keep in mind that Ansible EC2 module requires you to have Boto installed: 

    sudo pip install -U boto

You can specify AWS credentials either in Boto file (for example `~/.boto`) or using environment variables:
    
    AWS_ACCESS_KEY_ID='yourKeyId' AWS_SECRET_ACCESS_KEY='yourSecretKey' ansible-playbook aws.yml

## Installation 

    ansible-galaxy install hekonsek.fedora-ec2,0.6

## Role variables

- `instance_region` - AWS region to use. Default region is `eu-central-1`.
- `instance_name` - name tag for created instance. Default value is `defaultServer`.
- `instance_type` - instance type. Default value is `t2.medium`.
- `instance_ssd` - use ssd?. Default value is `true`.
- `keyName` - name that should be assigned to the uploaded SSH public key. Default value is `defaultKey`.
- `group` - name of the security group to create and use. Default value is `default`.
- `volume_size` - volume size in GB. Default value is `8`.

## Example playbook

```
- hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - { role: hekonsek.fedora-ec2,0.6 }
```

## License

Apache 2.0