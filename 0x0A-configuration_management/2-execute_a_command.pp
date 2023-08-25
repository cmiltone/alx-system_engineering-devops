# kills process killmenow

exec { 'killmenow'
  command: => 'pkill'
}