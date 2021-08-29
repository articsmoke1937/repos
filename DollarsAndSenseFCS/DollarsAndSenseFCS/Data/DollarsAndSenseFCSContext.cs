using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using DollarsAndSenseFCS.Models;

namespace DollarsAndSenseFCS.Data
{
    public class DollarsAndSenseFCSContext : DbContext
    {
        public DollarsAndSenseFCSContext (DbContextOptions<DollarsAndSenseFCSContext> options)
            : base(options)
        {
        }

        public DbSet<DollarsAndSenseFCS.Models.Contact> Contact { get; set; }
    }
}
