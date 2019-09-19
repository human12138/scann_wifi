# 详情

扫描周围WiFi的情况，如果周围WiFi少或者没有， 可多次运行该程序

# 配置

##### 启动`wpa_supplicant`应用，终端输入命令：

```
$ wpa_supplicant -D nl80211 -i wlan0 -c /etc/wpa_supplicant.conf -B
```

##### 打开`/etc/wpa_supplicant.conf`文件里，添加下面代码:

```
ctrl_interface=/var/run/wpa_supplicant
update_config=1
```

# 运行

```python
python3 scann_wifi.py
```

# 说明

网卡默认为wlan0，如果网卡不一致，可把程序中所有wlan0修改为需要扫描的设备的网卡。
