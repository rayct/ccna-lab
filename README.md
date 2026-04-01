# CCNA Lab Monitoring Stack

This repository contains a lightweight monitoring and automation stack designed to support a CCNA lab environment. It integrates network telemetry, visualization, and configuration management tools to provide observability and repeatability.

## Overview

The stack combines:

- **Prometheus** — metrics collection and time-series database
- **SNMP** — network device monitoring and telemetry
- **Grafana** — visualization and dashboarding
- **Ansible** — infrastructure automation and configuration management

## Architecture


[ Network Devices ]
|
SNMP
|
[ Prometheus ] ----> [ Grafana ]
|
Exporters / Targets

[ Ansible ]
|
Automation / Configuration Push


## Directory Structure


ccna-lab/
├── prometheus/     # Prometheus configuration and scrape targets
├── grafana/        # Dashboards and provisioning configs
├── snmp/           # SNMP configs / MIBs / exporters
├── ansible/        # Playbooks and inventory
└── README.md


## Components

### Prometheus
- Scrapes metrics from configured targets
- Integrates with SNMP exporters for network devices
- Configurable via `prometheus.yml`

### SNMP
- Used for polling routers, switches, and other lab devices
- Works in conjunction with Prometheus SNMP exporter

### Grafana
- Provides dashboards for:
  - Interface utilization
  - Device health
  - Network traffic patterns
- Connects to Prometheus as a data source

### Ansible
- Automates:
  - Device configuration
  - Deployment of monitoring components
  - Repeatable lab setup

## Usage

### 1. Configure Prometheus
Edit scrape targets:
```bash
prometheus/prometheus.yml
````

### 2. Start Services

(Example using Docker or local services depending on your setup)

### 3. Access Grafana

* Default: [http://localhost:3000](http://localhost:3000)
* Add Prometheus as a data source

### 4. Run Ansible Playbooks

```bash
ansible-playbook -i inventory site.yml
```

## Requirements

* Python 3.x
* Ansible
* Prometheus
* Grafana
* SNMP-enabled network devices or simulators (e.g. GNS3, EVE-NG)

## Future Improvements

* Alerting rules (Prometheus Alertmanager)
* Enhanced dashboards
* Role-based Ansible structure
* CI/CD integration

---

## Author

rayct

## Date

2026-04-01

```
