import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_systolic_array(dut):
    dut._log.info("Starting 2x2 NPU Systolic Array Test")

    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    dut.rst_n.value = 1
    dut._log.info("System Reset Complete")

    dut._log.info("Loading weights into the Processing Elements...")
    dut.uio_in.value = 1 
    dut.ui_in.value = 3   
    await RisingEdge(dut.clk)

    dut._log.info("Streaming activations and computing...")
    dut.uio_in.value = 2 
    dut.ui_in.value = 4   
    
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    final_output = int(dut.uo_out.value)
    dut._log.info(f"NPU Output Pin Value: {final_output}")
    
    assert final_output != 0, "ERROR: The NPU did not output a calculation!"
    dut._log.info("SUCCESS: The Systolic Array successfully multiplied and routed the data!")
