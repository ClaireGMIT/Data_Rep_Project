
use tablets;

CREATE TABLE tabprdn (
    -> Batch_No varchar(10) NOT NULL,
    -> API_Lot_No varchar(10) NOT NULL,
    -> API_Particle_Size enum('Large', 'Medium', 'Small') NOT NULL,
    -> Screen_Size enum('3', '4', '5') NOT NULL,
    -> Blend_Time float(3.1) NOT NULL,
    -> Compressor enum('Compress1', 'Compress2') NOT NULL,
    -> Inlet_Temp float(4.1) NOT NULL,
    -> Spray_Rate float(4.1) NOT NULL,
    -> Dissolution float(3.2) NOT NULL,
    -> PRIMARY KEY (Batch_No)
    -> );