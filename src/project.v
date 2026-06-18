/*
 * Copyright (c) 2024 R NAGA ARJUN
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_rknaga18_npu (
    input  wire [7:0] ui_in,    
    output wire [7:0] uo_out,   
    input  wire [7:0] uio_in,    
    output wire [7:0] uio_out,   
    output wire [7:0] uio_oe,   
    input  wire       ena,     
    input  wire       clk,      
    input  wire       rst_n     
);

  assign uo_out  = ui_in + uio_in;  
  assign uio_out = 0;
  assign uio_oe  = 0;

  wire _unused = &{ena, clk, rst_n, 1'b0};

endmodule
