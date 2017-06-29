Ansible Role - Fedora EC2 instance
=========

Provisions Fedora 25 on AWS EC2. It ensures that:
- Fedora 25 AWS EC2 node is provisioned and started
- public SSH key is uploaded and assigned to provisioned EC2 node
- EC2 security group firewall has been configured to accept only SSH traffic

Default instance size is T2 medium (i.e. 4 GB of RAM) - in order to change it, override `instance_type` Ansible variable (for example `instance_type=t2.large`).

Requirements
------------

Keep in mind that Ansible EC2 module requires you to have Boto installed: 

    sudo pip install -U boto

You can specify AWS credentials either in Boto file (for example `~/.boto`) or using environment variables:
    
    AWS_ACCESS_KEY_ID='yourKeyId' AWS_SECRET_ACCESS_KEY='yourSecretKey' ansible-playbook aws.yml

Role Variables
--------------

- `keyName` - name that should be assigned to the uploaded SSH public key 

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
