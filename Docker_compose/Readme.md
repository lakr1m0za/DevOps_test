You need create volume to mount in "server" dockerfile.
You need run command "docker volume create test_vol".
After that, you need run command "docker-cmpose up'.
After that, you need run command "docker inspect test_vol" and go to folder "Mountpoint".
DB files will be there.