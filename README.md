# Interact with postgres with Python

## Postgres setup

- Install:
```
  $ sudo pacman -Syy postgresql
```

- Add user to group: # not sure this is needed
```
  $ sudo usermod -a -G postgres aiara
```

- Login to the postgres user:
```
  $ sudo -iu postgres
```

- Initialize database cluster:
```
  [postgres]$ initdb -D /var/lib/postgres/data
  [postgres]$ exit
  pg_ctl -D /var/lib/postgres/data -l logfile start
```

- Start and enable the service
```
  $ sudo systemctl start postgresql.service
  $ sudo systemctl enable postgresql.service
```
