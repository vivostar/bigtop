class azkaban {
  class deploy ($roles) {
    if ('azkaban-solo-server' in $roles) {
      include azkaban::solo_server
    }

    if ('azkaban-web-server' in $roles) {
      include azkaban::web_server
    }

    if ('azkaban-exec-server' in $roles) {
      include azkaban::exec_server
    }
    
  }

  class solo_server {
    archive { '/tmp/azkaban-solo-server-3.90.0.tar.gz':
      ensure          => present,
      source          => 'puppet:///modules/azkaban/azkaban-solo-server-3.90.0.tar.gz',
      extract         => true,
      extract_command => 'tar xfz %s --strip-components=1',
      extract_path    => '/usr/lib/azkaban-solo-server',
      cleanup         => true,
    }
  }

  class web_server {
    archive { '/tmp/azkaban-web-server-3.90.0.tar.gz':
      ensure          => present,
      source          => 'puppet:///modules/azkaban/azkaban-web-server-3.90.0.tar.gz',
      extract         => true,
      extract_command => 'tar xfz %s --strip-components=1',
      extract_path    => '/usr/lib/azkaban-web-server',
      cleanup         => true,
    }
  }

  class exec_server {
    archive { '/tmp/azkaban-exec-server-3.90.0.tar.gz':
      ensure          => present,
      source          => 'puppet:///modules/azkaban/azkaban-exec-server-3.90.0.tar.gz',
      extract         => true,
      extract_command => 'tar xfz %s --strip-components=1',
      extract_path    => '/usr/lib/azkaban-exec-server',
      cleanup         => true,
    }
  }

}
