# installing a package

exec { 'apt-get update':
 command => '/usr/bin/apt-get update'
 path    => ['/usr/bin'],
 before  => Package['python3-pip'],
}

package { 'python3-pip':
  ensure => installed,
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}