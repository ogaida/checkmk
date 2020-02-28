# -*- encoding: utf-8 -*-

# yapf: disable
# type: ignore



checkname = 'ceph_status'


info = [[u'{'],
        [u'"health":', u'{'],
        [u'"health":', u'{'],
        [u'"health_services":', u'['],
        [u'{'],
        [u'"mons":', u'['],
        [u'{'],
        [u'"name":', u'"charon",'],
        [u'"kb_total":', u'72662176,'],
        [u'"kb_used":', u'4845960,'],
        [u'"kb_avail":', u'66764460,'],
        [u'"avail_percent":', u'91,'],
        [u'"last_updated":', u'"2017-04-11', u'09:51:22.695117",'],
        [u'"store_stats":', u'{'],
        [u'"bytes_total":', u'731100461,'],
        [u'"bytes_sst":', u'0,'],
        [u'"bytes_log":', u'1384653,'],
        [u'"bytes_misc":', u'729715808,'],
        [u'"last_updated":', u'"0.000000"'],
        [u'},'],
        [u'"health":', u'"HEALTH_OK"'],
        [u'},'],
        [u'{'],
        [u'"name":', u'"nix",'],
        [u'"kb_total":', u'74724384,'],
        [u'"kb_used":', u'4774220,'],
        [u'"kb_avail":', u'68869076,'],
        [u'"avail_percent":', u'92,'],
        [u'"last_updated":', u'"2017-04-11', u'09:50:58.026649",'],
        [u'"store_stats":', u'{'],
        [u'"bytes_total":', u'728622881,'],
        [u'"bytes_sst":', u'0,'],
        [u'"bytes_log":', u'969152,'],
        [u'"bytes_misc":', u'727653729,'],
        [u'"last_updated":', u'"0.000000"'],
        [u'},'],
        [u'"health":', u'"HEALTH_OK"'],
        [u'},'],
        [u'{'],
        [u'"name":', u'"hydra",'],
        [u'"kb_total":', u'74724384,'],
        [u'"kb_used":', u'4846784,'],
        [u'"kb_avail":', u'68796512,'],
        [u'"avail_percent":', u'92,'],
        [u'"last_updated":', u'"2017-04-11', u'09:51:25.695034",'],
        [u'"store_stats":', u'{'],
        [u'"bytes_total":', u'729631480,'],
        [u'"bytes_sst":', u'0,'],
        [u'"bytes_log":', u'2220377,'],
        [u'"bytes_misc":', u'727411103,'],
        [u'"last_updated":', u'"0.000000"'],
        [u'},'],
        [u'"health":', u'"HEALTH_OK"'],
        [u'}'],
        [u']'],
        [u'}'],
        [u']'],
        [u'},'],
        [u'"timechecks":', u'{'],
        [u'"epoch":', u'108,'],
        [u'"round":', u'31626,'],
        [u'"round_status":', u'"finished",'],
        [u'"mons":', u'['],
        [u'{'],
        [u'"name":', u'"charon",'],
        [u'"skew":', u'0.000000,'],
        [u'"latency":', u'0.000000,'],
        [u'"health":', u'"HEALTH_OK"'],
        [u'},'],
        [u'{'],
        [u'"name":', u'"nix",'],
        [u'"skew":', u'0.000000,'],
        [u'"latency":', u'0.000264,'],
        [u'"health":', u'"HEALTH_OK"'],
        [u'},'],
        [u'{'],
        [u'"name":', u'"hydra",'],
        [u'"skew":', u'0.000000,'],
        [u'"latency":', u'0.000274,'],
        [u'"health":', u'"HEALTH_OK"'],
        [u'}'],
        [u']'],
        [u'},'],
        [u'"summary":', u'['],
        [u'{'],
        [u'"severity":', u'"HEALTH_WARN",'],
        [u'"summary":',
         u'"too',
         u'many',
         u'PGs',
         u'per',
         u'OSD',
         u'(409',
         u'>',
         u'max',
         u'300)"'],
        [u'},'],
        [u'{'],
        [u'"severity":', u'"HEALTH_WARN",'],
        [u'"summary":',
         u'"pool',
         u'cephfs01',
         u'has',
         u'many',
         u'more',
         u'objects',
         u'per',
         u'pg',
         u'than',
         u'average',
         u'(too',
         u'few',
         u'pgs?)"'],
        [u'}'],
        [u'],'],
        [u'"overall_status":', u'"HEALTH_WARN",'],
        [u'"detail":', u'[]'],
        [u'},'],
        [u'"fsid":', u'"d9d08723-81e5-46b8-b2a4-b1590bc284c4",'],
        [u'"election_epoch":', u'108,'],
        [u'"quorum":', u'['],
        [u'0,'],
        [u'1,'],
        [u'2'],
        [u'],'],
        [u'"quorum_names":', u'['],
        [u'"charon",'],
        [u'"nix",'],
        [u'"hydra"'],
        [u'],'],
        [u'"monmap":', u'{'],
        [u'"epoch":', u'1,'],
        [u'"fsid":', u'"d9d08723-81e5-46b8-b2a4-b1590bc284c4",'],
        [u'"modified":', u'"0.000000",'],
        [u'"created":', u'"0.000000",'],
        [u'"mons":', u'['],
        [u'{'],
        [u'"rank":', u'0,'],
        [u'"name":', u'"charon",'],
        [u'"addr":', u'"10.249.12.121:6789\\/0"'],
        [u'},'],
        [u'{'],
        [u'"rank":', u'1,'],
        [u'"name":', u'"nix",'],
        [u'"addr":', u'"10.249.12.122:6789\\/0"'],
        [u'},'],
        [u'{'],
        [u'"rank":', u'2,'],
        [u'"name":', u'"hydra",'],
        [u'"addr":', u'"10.249.12.123:6789\\/0"'],
        [u'}'],
        [u']'],
        [u'},'],
        [u'"osdmap":', u'{'],
        [u'"osdmap":', u'{'],
        [u'"epoch":', u'95921,'],
        [u'"num_osds":', u'90,'],
        [u'"num_up_osds":', u'90,'],
        [u'"num_in_osds":', u'90,'],
        [u'"full":', u'false,'],
        [u'"nearfull":', u'false,'],
        [u'"num_remapped_pgs":', u'0'],
        [u'}'],
        [u'},'],
        [u'"pgmap":', u'{'],
        [u'"pgs_by_state":', u'['],
        [u'{'],
        [u'"state_name":', u'"active+clean",'],
        [u'"count":', u'6400'],
        [u'}'],
        [u'],'],
        [u'"version":', u'15285527,'],
        [u'"num_pgs":', u'6400,'],
        [u'"data_bytes":', u'9321031634464,'],
        [u'"bytes_used":', u'14768864055296,'],
        [u'"bytes_avail":', u'205284138250240,'],
        [u'"bytes_total":', u'220053002305536,'],
        [u'"read_bytes_sec":', u'291,'],
        [u'"read_op_per_sec":', u'0,'],
        [u'"write_op_per_sec":', u'0'],
        [u'},'],
        [u'"fsmap":', u'{'],
        [u'"epoch":', u'35,'],
        [u'"id":', u'1,'],
        [u'"up":', u'1,'],
        [u'"in":', u'1,'],
        [u'"max":', u'1,'],
        [u'"by_rank":', u'['],
        [u'{'],
        [u'"filesystem_id":', u'1,'],
        [u'"rank":', u'0,'],
        [u'"name":', u'"nix",'],
        [u'"status":', u'"up:active"'],
        [u'}'],
        [u'],'],
        [u'"up:standby":', u'2'],
        [u'}'],
        [u'}']]


discovery = {'': [(None, {})], 'mgrs': [], 'osds': [(None, {})], 'pgs': [(None, {})]}


checks = {'': [(None,
                {'epoch': (1, 3, 30)},
                [(1, 'Health: warning', []), (0, 'Epoch rate (30 m average): 0.00', [])])],
          'osds': [(None,
                    {'epoch': (50, 100, 15),
                     'num_down_osds': (7.0, 5.0),
                     'num_out_osds': (7.0, 5.0)},
                    [(0, 'Epoch rate (15 m average): 0.00', []),
                     (0, 'OSDs: 90, Remapped PGs: 0', []),
                     (0, 'OSDs out: 0, 0%', []),
                     (0, 'OSDs down: 0, 0%', [])])],
          'pgs': [(None, {}, [(0, "PGs: 6400, Status 'active+clean': 6400", [])])]}