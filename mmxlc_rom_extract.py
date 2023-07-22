#!/usr/bin/env python
import hashlib

int_sha512 = "905e1d515a77193a23a79d6d92b7e414dca04bb629adc43ca02138a5e26c780baec79b82ec111bb61db4b6f8a07be522ecb90592e864568455c4d12f8cbbfbae"
jp_sha512 = "07d069b4cc9f20b385cd4500d956c8b8fdeb62d4c4668fc5a302446e718d2338308913e360d887fa25e4766dcd4304025f73360d0e49126f71a0fe865cd3e293"

with open("RXC1.exe", "rb") as exe:

    # Calculate checksum and determine version and offsets
    
    sha512sum = hashlib.sha512(exe.read()).hexdigest()
    if int_sha512 == sha512sum:
        print("Checksum matches international release, using those offsets for extraction...")
        
        rx1_start   = 0xB8C4E0
        rx1r1_start = 0xD0C4E0
        mx1_start   = 0xD8C4E0
        mx1r1_start = 0xF0C4E0
        rx2_start   = 0xF8C4E0
        mx2_start  = 0x110C4E0
        rx3_start  = 0x128C4E0
        mx3_start  = 0x148C4E0

    elif jp_sha512 == sha512sum:
        print("Checksum matches Japanese release, using those offsets for extraction...")
        rx1_start  = 0xB8C750
        mx1_start  = 0xD8C750
        rx2_start  = 0xF8C750
        mx2_start = 0x110C750
        rx3_start = 0x128C750
        mx3_start = 0x148C750

    else:
        print("Checksum doesn't match any known values, exiting.")
        print(sha512sum)
        exit()

    # Extract ROM data to files using offsets

    filename = "Rock Man X.sfc"
    with open(filename, "wb") as out:
        exe.seek(rx1_start,0)
        out.write(exe.read(0x180000))
        out.close()
        print("Extracted " + filename)
    
    filename = "Mega Man X.sfc"
    with open(filename, "wb") as out:
        exe.seek(mx1_start,0)
        out.write(exe.read(0x180000))
        out.close()
        print("Extracted " + filename)

    filename = "Rock Man X2.sfc"
    with open(filename, "wb") as out:
        exe.seek(rx2_start,0)
        out.write(exe.read(0x180000))
        out.close()
        print("Extracted " + filename)

    filename = "Mega Man X2.sfc"
    with open(filename, "wb") as out:
        exe.seek(mx2_start,0)
        out.write(exe.read(0x180000))
        out.close()
        print("Extracted " + filename)

    filename = "Rock Man X3.sfc"
    with open(filename, "wb") as out:
        exe.seek(rx3_start,0)
        out.write(exe.read(0x200000))
        out.close()
        print("Extracted " + filename)

    filename = "Mega Man X3.sfc"
    with open(filename, "wb") as out:
        exe.seek(mx3_start,0)
        out.write(exe.read(0x200000))
        out.close()
        print("Extracted " + filename)

    if int_sha512 == sha512sum:
    
        filename = "Rock Man X r1.sfc"
        with open(filename, "wb") as out:
            exe.seek(rx1r1_start,0)
            out.write(exe.read(0x80000))
            exe.seek(rx1_start + 0x80000,0)
            out.write(exe.read(0x100000))
            out.close()
            print("Extracted " + filename)

        filename = "Mega Man X r1.sfc"
        with open(filename, "wb") as out:
            exe.seek(mx1r1_start,0)
            out.write(exe.read(0x80000))
            exe.seek(mx1_start + 0x80000,0)
            out.write(exe.read(0x100000))
            out.close()
            print("Extracted " + filename)

    exe.close()