# Docker on Ubuntu 18.04

This playbook will install Docker an Ubuntu 18.04 machine, as explained in the guide on
A number of containers will be created with the options specified in the `vars/default.yml` variable file.

## Settings

- `create_containers`: number of containers to create.
- `default_container_name`: default name for new containers.
- `default_container_image`: default image for new containers.
- `default_container_command`: default command to run on new containers.


### Customize Options

```shell
nano vars/default.yml
```

```yml
#vars/default.yml
---
create_containers: 4
default_container_name: docker
default_container_image: ubuntu
default_container_command: sleep 1d
```

### Run the Playbook

```command
ansible-playbook -l [target] -i [inventory file] -u [remote user] playbook.yml
```
