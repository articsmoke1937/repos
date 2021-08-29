﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace DollarsAndSenseFCS.Models
{
    public class Contact
    {
        public int ID { get; set; }
        public string Name { get; set; }

        [DataType(Datatype.date)]
        public DateTime Date { get; set; }
        public string PhoneNumber { get; set; }
        public string Email { get; set; }
    }
}
