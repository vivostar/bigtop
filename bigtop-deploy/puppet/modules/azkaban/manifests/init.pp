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

    if ('azkaban-db' in $roles) {
      include azkaban::db
    }
    
  }

  class solo_server {
    file {'/tmp/azkaban-solo-server-3.90.0.tar.gz':
      ensure        => present,
      source        => "puppet:///modules/azkaban/azkaban-solo-server-3.90.0.tar.gz",
    }

    file {'/usr/lib/azkaban-solo-server':
      ensure        => directory,
    }

    archive { '/tmp/azkaban-solo-server.tar.gz':
      ensure          => present,
      source          => "/tmp/azkaban-solo-server-3.90.0.tar.gz",
      extract         => true,
      extract_command => 'tar xfz %s --strip-components=1',
      extract_path    => '/usr/lib/azkaban-solo-server',
      cleanup         => true,
      require         => [
        File['/tmp/azkaban-solo-server-3.90.0.tar.gz'],
        File['/usr/lib/azkaban-solo-server'],
      ],
    }
  }

  class web_server {
    file {'/tmp/azkaban-web-server-3.90.0.tar.gz':
      ensure        => present,
      source        => "puppet:///modules/azkaban/azkaban-web-server-3.90.0.tar.gz",
    }

    file {'/usr/lib/azkaban-web-server':
      ensure        => directory,
    }

    archive { '/tmp/azkaban-web-server.tar.gz':
      ensure          => present,
      source          => "/tmp/azkaban-web-server-3.90.0.tar.gz",
      extract         => true,
      extract_command => 'tar xfz %s --strip-components=1',
      extract_path    => '/usr/lib/azkaban-web-server',
      cleanup         => true,
      require         => [
        File['/tmp/azkaban-web-server-3.90.0.tar.gz'],
        File['/usr/lib/azkaban-web-server'],
      ],
    }

  }

  class exec_server {
    file {'/tmp/azkaban-exec-server-3.90.0.tar.gz':
      ensure        => present,
      source        => "puppet:///modules/azkaban/azkaban-exec-server-3.90.0.tar.gz",
    }

    file {'/usr/lib/azkaban-exec-server':
      ensure        => directory,
    }

    archive { '/tmp/azkaban-exec-server.tar.gz':
      ensure          => present,
      source          => "/tmp/azkaban-exec-server-3.90.0.tar.gz",
      extract         => true,
      extract_command => 'tar xfz %s --strip-components=1',
      extract_path    => '/usr/lib/azkaban-exec-server',
      cleanup         => true,
      require         => [
        File['/tmp/azkaban-exec-server-3.90.0.tar.gz'],
        File['/usr/lib/azkaban-exec-server'],
      ],
    }
  }

  class db {

    file {'/tmp/azkaban-db-3.90.0.tar.gz':
      ensure        => present,
      source        => "puppet:///modules/azkaban/azkaban-db-3.90.0.tar.gz",
    }

    file {'/usr/lib/azkaban-db':
      ensure        => directory,
    }

    archive { '/tmp/azkaban-db.tar.gz':
      ensure          => present,
      source          => "/tmp/azkaban-db-3.90.0.tar.gz",
      extract         => true,
      extract_command => 'tar xfz %s --strip-components=1',
      extract_path    => '/usr/lib/azkaban-db',
      cleanup         => true,
      require         => [
        File['/tmp/azkaban-db-3.90.0.tar.gz'],
        File['/usr/lib/azkaban-db'],
      ],
    }

  }

}
