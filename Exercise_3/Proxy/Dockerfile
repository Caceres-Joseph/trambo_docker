FROM nginx

LABEL maintainer="Joseph Cáceres<josephccaceres@gmail.com>"

#Delete the existing default.conf
RUN rm /etc/nginx/conf.d/default.conf

#Copy the custom default.conf to the nginx configuration
COPY default.conf /etc/nginx/conf.d

