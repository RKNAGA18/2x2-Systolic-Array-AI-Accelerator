# Physical Layout Specifications

This directory contains the physical GDSII layout and rendering of the 2x2 Systolic Array macro, targeted for the SkyWater 130nm open-source PDK.

## Macro Details
* **Foundry PDK:** SkyWater 130nm (`sky130_fd_sc_hd`)
* **Standard Cell Library:** High Density (HD)
* **DRC / LVS Status:** Clean (Passed Tiny Tapeout Precheck)

## Physical Interface (Pinout)
If integrating this GDSII macro into a larger System-on-Chip (SoC) or testing on a silicon breakout board, use the following pin mappings:

| Port | Width | Direction | Function |
| :--- | :--- | :--- | :--- |
| `clk` | 1-bit | Input | System Clock (Max 50 MHz) |
| `rst_n` | 1-bit | Input | Active-Low System Reset |
| `ui_in` | 8-bit | Input | Dedicated Input (Used for Activation streaming) |
| `uio_in` | 8-bit | Input | Bidirectional IO (Used for Control Signals) |
| `uo_out` | 8-bit | Output | Dedicated Output (Used for reading MAC results) |

### Control Signal Mapping (`uio_in`)
* `uio_in[0]`: **weight_load** (Set HIGH to latch `ui_in` to the weight registers)
* `uio_in[1]`: **compute_en** (Set HIGH to stream `ui_in` as activation data)
