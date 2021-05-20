docker network create \
    --driver=overlay \
    website_network

docker service create \
    --name redis \
    --network website_network \
    --replicas=1 \
    redislabs/rejson:latest

docker service create \
    --name web-server \
    --network website_network \
    --replicas=2 \
    --publish published=80,target=80 \
    --env REPO_LINK=https://api.github.com/users/mandrelbrotset/repos \
    --env REDIS_HOST=redis \
    public.ecr.aws/g6t3v7d2/website/web-server