# WITRN driver

Driver for reading data from modern WITRN USB-meters
such as U3, U3L, A2, and C4 (tested). A2L and C4L can
also be supported theoretically but I don't have hardware
for testing.

## Supported hardware

* Tested by community:
  * [WITRN U3 & U3L](https://www.witrn.com/?p=92)
  * [WITRN A2](https://www.witrn.com/?p=88)
  * [WITRN C4](https://www.witrn.com/?p=2169)
  * [WITRN K2](https://www.witrn.com/?p=2105)
* Not tested bot probably should works:
  * [WITRN A2L](https://www.witrn.com/?p=88)

## Installation

Available on PyPI:
```shell
pip install witrn-driver
```

Driver can be installed as python package
using  `pip install -e` for local development.

## Related projects

* [Bokeh-based UI](https://github.com/Fescron/witrn-ui-bokeh) by [@Fescron](https://github.com/Fescron)

## Examples

Sample output of [`exmaples/read_data.py`](examples/read_data.py):

```
Connect your device and press Enter
No kernel driver attached
Claimed device
Press Enter to stop reading

 packets |      rectime |       uptime |      V      A |     D+     D-
   23755 |  0:03:57.074 |  3:10:55.199 |  5.158  0.004 |  2.717  2.706

Good bye!
```

## Limitations

**Note!** For Windows users, if you see message `Device not found!` when device is
actually connected, try use [zadig](https://github.com/pbatard/libwdi/releases)
utility and replace the default driver for your WITRN device to `libusb-*`.

**Note!** For Linux users, to run this script under non-root user install udev rules:

```shell
$ sudo install --mode=0644 --target-directory=/etc/udev/rules.d/ udev/90-usbmeter.rules
$ sudo udevadm trigger
```
