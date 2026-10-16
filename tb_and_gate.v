module tb_and_gate;
    reg a, b;
    wire y;

    and_gate dut(.a(a), .b(b), .y(y));

    initial begin
        a=0; b=0; #10;
        if (y !== 0) $fatal(1, "Test 00 failed");

        a=0; b=1; #10;
        if (y !== 0) $fatal(1, "Test 01 failed");

        a=1; b=0; #10;
        if (y !== 0) $fatal(1, "Test 10 failed");

        a=1; b=1; #10;
        if (y !== 1) $fatal(1, "Test 11 failed");

        $display("ALL 4 TESTS PASSED");
        $finish;
    end
endmodule
