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
    public class DetailsModel : PageModel
    {
        private readonly DollarsAndSenseFCS.Data.DollarsAndSenseFCSContext _context;

        public DetailsModel(DollarsAndSenseFCS.Data.DollarsAndSenseFCSContext context)
        {
            _context = context;
        }

        public Contact Contact { get; set; }

        public async Task<IActionResult> OnGetAsync(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            Contact = await _context.Contact.FirstOrDefaultAsync(m => m.ID == id);

            if (Contact == null)
            {
                return NotFound();
            }
            return Page();
        }
    }
}
