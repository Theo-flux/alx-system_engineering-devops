# create a file in /tmp.

file { '/tmp/school':c
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
