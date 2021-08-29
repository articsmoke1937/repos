using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using DollarsAndSenseFCS.Data;
using DollarsAndSenseFCS.Models;

namespace DollarsAndSenseFCS.Pages.Contact
{
    public class IndexModel : PageModel
    {
        private readonly DollarsAndSenseFCS.Data.DollarsAndSenseFCSContext _context;

        public IndexModel(DollarsAndSenseFCS.Data.DollarsAndSenseFCSContext context)
        {
            _context = context;
        }

        public IList<Contact> Contact { get;set; }

        public async Task OnGetAsync()
        {
            Contact = await _context.Contact.ToListAsync();
        }
    }
}
