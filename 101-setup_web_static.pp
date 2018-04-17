# This script installs a server for web_static

package { 'nginx':
    ensure => 'installed',
}
service { 'nginx':
    ensure => 'running',
}

file { ['/data/', '/data/web_static/', '/data/web_static/releases/',
        '/data/web_static/shared/', '/data/web_static/releases/test/']:
    ensure => 'directory',
}

exec { 'test_index_html':
    path    => '/bin:/usr/bin:/sbin:/usr/sbin:',
    command => 'sudo mkdir -p /data/web_static/releases/test && sudo echo "testing 123" > /data/web_static/releases/test/index.html',
}

file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test/'
}

exec { 'permissions':
    path    => '/bin:/usr/bin:/sbin:/usr/sbin:',
    command => 'sudo chown -R ubuntu:ubuntu /data/',
}

exec { 'update_nginx_config':
    path    => '/bin:/usr/bin:/sbin:/usr/sbin:',
    command => 'sudo sed -i "42i location /hbnb_static {\n alias /data/web_static/current;\n}" /etc/nginx/sites-enabled/default && sudo service nginx restart'
}
