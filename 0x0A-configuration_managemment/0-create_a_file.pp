# create a file in /tmp.
file { '/school':
  ensure  => file,
  path    => '/tmp',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}