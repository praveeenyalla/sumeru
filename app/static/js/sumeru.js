/**
 * Sumeru Technologies — Corporate Client Interactive Script
 * Principle: "SIMPLE ON THE SURFACE. DEEP UNDERNEATH."
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileMenu();
  init4DApproach();
  initContactForm();
  initMegaMenuAccessibility();
  initExpandableCards();
});

/**
 * 1. Sticky Header Behavior
 * Transparent/integrated at top, solid white with subtle shadow when scrolled
 */
function initStickyHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  const onScroll = () => {
    if (window.scrollY > 20) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/**
 * 2. Mobile Navigation Drawer & Accordion Submenus
 */
function initMobileMenu() {
  const toggleBtn = document.querySelector('.mobile-menu-toggle');
  const drawer = document.querySelector('.mobile-nav-drawer');
  const overlay = document.querySelector('.mobile-nav-overlay');
  const closeBtn = document.querySelector('.mobile-nav-close');

  if (!toggleBtn || !drawer || !overlay) return;

  const openDrawer = () => {
    drawer.classList.add('open');
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  };

  const closeDrawer = () => {
    drawer.classList.remove('open');
    overlay.classList.remove('open');
    document.body.style.overflow = '';
  };

  toggleBtn.addEventListener('click', openDrawer);
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  overlay.addEventListener('click', closeDrawer);

  // Accordions in mobile drawer
  const accordionHeaders = document.querySelectorAll('.mobile-accordion-header');
  accordionHeaders.forEach(btn => {
    btn.addEventListener('click', () => {
      const content = btn.nextElementSibling;
      const isOpen = content.classList.contains('open');
      
      // Close other accordions
      document.querySelectorAll('.mobile-accordion-content').forEach(c => c.classList.remove('open'));
      
      if (!isOpen) {
        content.classList.add('open');
      }
    });
  });
}

/**
 * 3. 4D Business Approach Interactive Timeline
 * Discover, Design, Deploy, Drive
 */
const APPROACH_DATA = {
  discover: {
    badge: "STAGE 01 — UNDERSTAND & SCOPE",
    heading: "Discover: Analyzing Business Objectives & Opportunities",
    body: "Sumeru Technologies works with you in partnership to understand your business, your existing technology, and your challenges and opportunities. This effort includes an analysis of industry trends, your existing technology infrastructure, organizational structure, immediate/long-term needs, and your vision for the future. The Sumeru Technologies team makes recommendations on initiatives that will maximize business impact. Through further discussion, this is translated into the clear vision and scope of the project.",
    highlights: [
      "Enterprise infrastructure & technical debt assessment",
      "Analysis of organizational structure & operational workflows",
      "Identification of immediate quick wins and multi-year strategic roadmap",
      "Collaborative project scope definition and executive alignment"
    ]
  },
  design: {
    badge: "STAGE 02 — ARCHITECTURE & BLUEPRINT",
    heading: "Design: Engineering Scalable, Future-Proof Solutions",
    body: "At this point alternatives are crafted to address your specific business opportunities. Our architected approach ensures a complete, scalable solution, one that integrates with your current environment and maps uniquely to your business initiatives. Design creates for you a competitive and strategic game plan. The end result is a well-articulated IT solution to the challenges facing your organization.",
    highlights: [
      "Solution blueprinting integrating seamlessly with existing ERP/legacy stack",
      "Evaluation of package vs custom build options to eliminate runaway cost",
      "Clean Core architecture preventing vendor lock-in and upgrade friction",
      "Security, compliance, and multi-tier disaster recovery planning"
    ]
  },
  deploy: {
    badge: "STAGE 03 — IMPLEMENTATION & RIGOR",
    heading: "Deploy: On-Time, On-Budget Solution Delivery",
    body: "With your requirements, approach and architecture defined, Sumeru Technologies applies experience and technical savvy to deploy your solution. Processes based upon industry best practices and our Solution Delivery tool sets keep your efforts on track and under control. The results — projects delivered on time, on-schedule and on the mark with quantified returns and direct business impacts.",
    highlights: [
      "Agile and phased execution governed by PMP and certified Scrum directors",
      "Rigorous quality assurance, automated test regression, and user acceptance",
      "Change management and comprehensive employee transition training",
      "Single point of accountability across hardware, software, and integration"
    ]
  },
  drive: {
    badge: "STAGE 04 — CONTINUOUS VALUE & 24x7 OPS",
    heading: "Drive: Ongoing Optimization & Global Managed Operations",
    body: "In the modern paradigm, your IT infrastructure is mission critical and hence needs to be managed and enhanced constantly. With your solution implemented, Sumeru Technologies provides post transition training, 24X7 application and infrastructure support, help-desk services, and systems operations. One of our National Practices is focused on Outsourcing and is capable of freeing you from daily systems management, allowing you to concentrate on your most strategic business programs.",
    highlights: [
      "24x7 remote database, ERP, and infrastructure management",
      "Dedicated offshore delivery teams in Hyderabad and Bangalore",
      "Proactive systems monitoring, patch management, and SLA enforcement",
      "Continuous process benchmarking and iterative enhancement"
    ]
  }
};

function init4DApproach() {
  const stepButtons = document.querySelectorAll('.approach-step-btn');
  const panel = document.querySelector('.approach-card-panel');
  if (!stepButtons.length || !panel) return;

  stepButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const stepKey = btn.dataset.step;
      const data = APPROACH_DATA[stepKey];
      if (!data) return;

      // Update button active state
      stepButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      // Update panel content with smooth fade
      panel.style.opacity = '0.5';
      setTimeout(() => {
        const badgeEl = panel.querySelector('.approach-panel-badge');
        const headingEl = panel.querySelector('.approach-panel-heading');
        const bodyEl = panel.querySelector('.approach-panel-body');
        const listEl = panel.querySelector('.approach-highlights-list');

        if (badgeEl) badgeEl.textContent = data.badge;
        if (headingEl) headingEl.textContent = data.heading;
        if (bodyEl) bodyEl.textContent = data.body;
        
        if (listEl) {
          listEl.innerHTML = data.highlights.map(item => `
            <li>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
              <span>${item}</span>
            </li>
          `).join('');
        }
        panel.style.opacity = '1';
      }, 150);
    });
  });
}

/**
 * 4. Contact Form AJAX Submission with Backend Integration
 */
function initContactForm() {
  const form = document.getElementById('sumeru-contact-form');
  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const submitBtn = form.querySelector('button[type="submit"]');
    const feedbackBox = document.getElementById('form-feedback');
    const originalText = submitBtn.innerHTML;

    // Collect data
    const formData = {
      full_name: form.elements['full_name'].value.trim(),
      company: form.elements['company'].value.trim(),
      business_email: form.elements['business_email'].value.trim(),
      phone: form.elements['phone'] ? form.elements['phone'].value.trim() : '',
      service_interested_in: form.elements['service_interested_in'].value,
      message: form.elements['message'].value.trim()
    };

    if (!formData.full_name || !formData.company || !formData.business_email || !formData.message) {
      if (feedbackBox) {
        feedbackBox.className = 'form-feedback error';
        feedbackBox.textContent = 'Please fill out all required fields.';
        feedbackBox.style.display = 'block';
      }
      return;
    }

    try {
      submitBtn.disabled = true;
      submitBtn.innerHTML = 'Sending Inquiry...';

      const response = await fetch('/api/contact/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });

      const result = await response.json();

      if (response.ok) {
        if (feedbackBox) {
          feedbackBox.className = 'form-feedback success';
          feedbackBox.innerHTML = `<strong>Inquiry Dispatched Successfully!</strong><br/>Reference ID: <code>${result.reference_id}</code>.<br/>${result.message}`;
          feedbackBox.style.display = 'block';
        }
        form.reset();
      } else {
        throw new Error(result.detail || 'Failed to submit inquiry.');
      }
    } catch (err) {
      if (feedbackBox) {
        feedbackBox.className = 'form-feedback error';
        feedbackBox.textContent = err.message || 'A network error occurred. Please try again or contact HR@sumerutechnologies.com directly.';
        feedbackBox.style.display = 'block';
      }
    } finally {
      submitBtn.disabled = false;
      submitBtn.innerHTML = originalText;
    }
  });
}

/**
 * 5. Mega Menu Accessibility & Robust Interaction
 * - Debounced hover to prevent premature collapse
 * - Click-to-lock/toggle behavior
 * - Closes on link selection, outside click, or Escape key
 */
function initMegaMenuAccessibility() {
  const navItems = document.querySelectorAll('.nav-item');
  const siteHeader = document.querySelector('.site-header');
  let closeTimeout = null;
  let hoverOpenTimeout = null;
  let currentlyLockedItem = null;

  const closeAllMenus = () => {
    if (closeTimeout) {
      clearTimeout(closeTimeout);
      closeTimeout = null;
    }
    if (hoverOpenTimeout) {
      clearTimeout(hoverOpenTimeout);
      hoverOpenTimeout = null;
    }
    navItems.forEach(item => {
      item.classList.remove('menu-locked', 'menu-open', 'hover-active');
      const mega = item.querySelector('.mega-menu');
      if (mega) {
        mega.style.opacity = '';
        mega.style.visibility = '';
        mega.style.pointerEvents = '';
      }
    });
    currentlyLockedItem = null;
  };

  const openMenu = (item, lock = false) => {
    const mega = item.querySelector('.mega-menu');
    if (!mega) return;

    if (closeTimeout) {
      clearTimeout(closeTimeout);
      closeTimeout = null;
    }

    // Close any other open menu
    navItems.forEach(other => {
      if (other !== item) {
        other.classList.remove('menu-locked', 'menu-open', 'hover-active');
        const otherMega = other.querySelector('.mega-menu');
        if (otherMega) {
          otherMega.style.opacity = '';
          otherMega.style.visibility = '';
          otherMega.style.pointerEvents = '';
        }
      }
    });

    item.classList.add('menu-open', 'hover-active');
    if (lock) {
      item.classList.add('menu-locked');
      currentlyLockedItem = item;
    }
    mega.style.opacity = '1';
    mega.style.visibility = 'visible';
    mega.style.pointerEvents = 'auto';
  };

  navItems.forEach(item => {
    const link = item.querySelector('.nav-link');
    const mega = item.querySelector('.mega-menu');
    if (!link || !mega) return;

    // Click behavior: toggle lock
    link.addEventListener('click', (e) => {
      e.preventDefault(); // Prevent navigating top-level parent link if it has a mega menu
      const isAlreadyLocked = item.classList.contains('menu-locked');
      if (isAlreadyLocked) {
        closeAllMenus();
      } else {
        openMenu(item, true);
      }
    });

    // Mouseenter on nav item:
    item.addEventListener('mouseenter', () => {
      if (closeTimeout) {
        clearTimeout(closeTimeout);
        closeTimeout = null;
      }

      // If an item is already locked, only switch if user deliberately dwells on new item for 400ms
      if (currentlyLockedItem && currentlyLockedItem !== item) {
        if (hoverOpenTimeout) clearTimeout(hoverOpenTimeout);
        hoverOpenTimeout = setTimeout(() => {
          openMenu(item, false);
        }, 350);
        return;
      }

      // If this item is already open, cancel any close
      if (item.classList.contains('menu-open')) return;

      // Normal hover: smooth 100ms dwell before opening
      if (hoverOpenTimeout) clearTimeout(hoverOpenTimeout);
      hoverOpenTimeout = setTimeout(() => {
        openMenu(item, false);
      }, 100);
    });

    // Mouseleave on nav item:
    item.addEventListener('mouseleave', (e) => {
      if (hoverOpenTimeout) {
        clearTimeout(hoverOpenTimeout);
        hoverOpenTimeout = null;
      }

      // Check if moving into the mega-menu of this item
      const toEl = e.relatedTarget;
      if (toEl && (mega.contains(toEl) || mega === toEl)) {
        return; // Transitioning directly into submenu
      }

      // If locked, do not auto-close on mouseleave
      if (item.classList.contains('menu-locked')) return;

      // Grace period of 400ms before closing
      closeTimeout = setTimeout(() => {
        if (!item.classList.contains('menu-locked')) {
          item.classList.remove('menu-open', 'hover-active');
          mega.style.opacity = '';
          mega.style.visibility = '';
          mega.style.pointerEvents = '';
        }
      }, 400);
    });

    // Entering the mega-menu itself preserves open state
    mega.addEventListener('mouseenter', () => {
      if (closeTimeout) {
        clearTimeout(closeTimeout);
        closeTimeout = null;
      }
      item.classList.add('menu-open', 'hover-active');
    });

    // Leaving the mega-menu
    mega.addEventListener('mouseleave', (e) => {
      const toEl = e.relatedTarget;
      if (toEl && (item.contains(toEl) || item === toEl)) {
        return; // Moving back up to nav link
      }

      if (item.classList.contains('menu-locked')) return;

      closeTimeout = setTimeout(() => {
        if (!item.classList.contains('menu-locked')) {
          item.classList.remove('menu-open', 'hover-active');
          mega.style.opacity = '';
          mega.style.visibility = '';
          mega.style.pointerEvents = '';
        }
      }, 400);
    });

    // Submenu links: close menu on link selection
    const sublinks = mega.querySelectorAll('a');
    sublinks.forEach(sub => {
      sub.addEventListener('click', () => {
        closeAllMenus();
      });
    });

    // Keyboard tab navigation
    link.addEventListener('focus', () => {
      openMenu(item, false);
    });
  });

  // Click outside header closes all locked menus
  document.addEventListener('click', (e) => {
    const isInsideHeader = e.target.closest('.site-header');
    if (!isInsideHeader) {
      closeAllMenus();
    }
  });

  // Escape key closes menus
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeAllMenus();
    }
  });
}

/**
 * 6. Interactive Vertical Rectangular Content Card System (Section 8)
 * Principle: "ELEGANT VERTICAL CARDS. RICH FLOATING RECTANGULAR DEEP-DIVE."
 */
function initExpandableCards() {
  const cards = document.querySelectorAll('.vcard');
  const overlay = document.getElementById('vcard-overlay');
  const panelBody = document.getElementById('floating-panel-body');
  const badgeEl = document.getElementById('floating-panel-badge');
  const hashEl = document.getElementById('floating-panel-hash');
  const closeBtn = document.getElementById('floating-panel-close-btn');
  const bottomCloseBtn = document.getElementById('floating-panel-bottom-close');
  
  if (!cards.length) return;

  // Load topics data from JSON script tag
  let topicsData = [];
  const scriptTag = document.getElementById('sumeru-topics-data');
  if (scriptTag) {
    try {
      topicsData = JSON.parse(scriptTag.textContent || '[]');
    } catch (err) {
      console.warn('Failed to parse sumeru-topics-data:', err);
    }
  }

  // Map by id and slug
  const topicsMap = new Map();
  topicsData.forEach(t => {
    if (t.id) topicsMap.set(t.id, t);
    if (t.slug) topicsMap.set(t.slug, t);
  });

  const escapeHtml = (unsafe) => {
    if (typeof unsafe !== 'string') return unsafe || '';
    return unsafe
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  };

  let lastFocusedElement = null;

  const openCardModal = (cardId) => {
    const data = topicsMap.get(cardId);
    if (!data || !overlay || !panelBody) {
      // Fallback: smooth scroll to existing article in page if data not in JSON
      const fallbackTarget = document.getElementById(cardId);
      if (fallbackTarget) {
        fallbackTarget.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
      return;
    }

    lastFocusedElement = document.activeElement;

    // Header updates
    if (badgeEl) badgeEl.textContent = data.badge || 'ENTERPRISE PRACTICE';
    if (hashEl) hashEl.textContent = '#' + (data.id || cardId);

    // Build rich HTML body
    let bodyHtml = '';

    // 1. Large Top Image with Caption
    if (data.image && data.image.url) {
      bodyHtml += `
        <div class="floating-panel-image-wrap">
          <img src="${data.image.url}" alt="${data.image.alt || data.title}" class="floating-panel-image" loading="lazy" />
          ${data.image.caption ? `<div class="floating-panel-caption">${data.image.caption}</div>` : ''}
        </div>
      `;
    }

    // 2. Title & Lead
    bodyHtml += `
      <div>
        <h2 class="floating-panel-title">${data.title}</h2>
        ${data.lead ? `<p class="floating-panel-lead">${data.lead}</p>` : ''}
      </div>
    `;

    // 3. Researched Content / Narrative Sections
    if (Array.isArray(data.content_sections) && data.content_sections.length > 0) {
      data.content_sections.forEach(sec => {
        bodyHtml += `
          <div class="floating-panel-section">
            <h3 class="floating-panel-section-title">${sec.heading}</h3>
            <div class="floating-panel-section-text">${sec.body.replace(/\n\n/g, '<br/><br/>')}</div>
          </div>
        `;
      });
    } else if (Array.isArray(data.content)) {
      data.content.forEach(sec => {
        bodyHtml += `
          <div class="floating-panel-section">
            ${sec.heading ? `<h3 class="floating-panel-section-title">${sec.heading}</h3>` : ''}
            <div class="floating-panel-section-text">${(sec.body || '').replace(/\n\n/g, '<br/><br/>')}</div>
          </div>
        `;
      });
    } else if (typeof data.content === 'string' && data.content) {
      bodyHtml += `
        <div class="floating-panel-section">
          <div class="floating-panel-section-text">${data.content.replace(/\n\n/g, '<br/><br/>')}</div>
        </div>
      `;
    }

    // 4. Operational Methodology Stages (e.g. 4D or Practice Steps)
    if (Array.isArray(data.methodology) && data.methodology.length > 0) {
      bodyHtml += `
        <div class="floating-panel-section">
          <h4 style="font-size: 0.8125rem; font-weight: 800; color: #004A7F; letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 8px;">
            Execution Methodology &amp; Engineering Stages
          </h4>
          <div class="floating-methodology-grid">
            ${data.methodology.map(m => `
              <div class="floating-methodology-step">
                <div class="floating-methodology-num">${m.step}</div>
                <div class="floating-methodology-name">${m.name}</div>
                <p class="floating-methodology-desc">${m.desc}</p>
              </div>
            `).join('')}
          </div>
        </div>
      `;
    }

    // 5. Technologies & Deliverables Grid
    const hasTech = Array.isArray(data.technologies) && data.technologies.length > 0;
    const hasDeliv = Array.isArray(data.deliverables) && data.deliverables.length > 0;

    if (hasTech || hasDeliv) {
      bodyHtml += `<div class="floating-meta-grid">`;
      
      if (hasTech) {
        bodyHtml += `
          <div class="floating-meta-box">
            <h5 class="floating-meta-box-title">Supported Technologies &amp; Standards</h5>
            <div class="floating-pill-list">
              ${data.technologies.map(t => `<span class="floating-pill">${t}</span>`).join('')}
            </div>
          </div>
        `;
      }

      if (hasDeliv) {
        bodyHtml += `
          <div class="floating-meta-box">
            <h5 class="floating-meta-box-title">Enterprise Client Deliverables</h5>
            <ul class="floating-checklist">
              ${data.deliverables.map(d => `
                <li class="floating-checklist-item">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#69B531" stroke-width="2.5" style="flex-shrink: 0; margin-top: 2px;">
                    <polyline points="20 6 9 17 4 12"></polyline>
                  </svg>
                  <span>${d}</span>
                </li>
              `).join('')}
            </ul>
          </div>
        `;
      }

      bodyHtml += `</div>`;
    }

    // 6. Topic Specific Q&A Governance
    if (data.qa && data.qa.q && data.qa.a) {
      bodyHtml += `
        <div class="floating-qa-box">
          <div class="floating-qa-tag">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <circle cx="12" cy="12" r="10"></circle>
              <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
              <line x1="12" y1="17" x2="12.01" y2="17"></line>
            </svg>
            <span>EXACT PRACTICE GOVERNANCE</span>
          </div>
          <div class="floating-qa-q">${data.qa.q}</div>
          <p class="floating-qa-a">${data.qa.a}</p>
        </div>
      `;
    }

    // 7. Verified Sources & Public References (Attribution)
    if (Array.isArray(data.sources) && data.sources.length > 0) {
      bodyHtml += `
        <div class="floating-sources-box">
          <div class="floating-sources-title">Verified Sources &amp; Public References:</div>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 6px;">
            ${data.sources.map(s => `
              <li>
                <a href="${s.url}" target="_blank" rel="noopener noreferrer" class="floating-source-link">
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
                  <span>${s.title}</span>
                </a>
                <span class="floating-source-meta">(${s.sourceType}${s.retrievedAt ? ` &bull; Ref ${s.retrievedAt.slice(0, 10)}` : ''})</span>
              </li>
            `).join('')}
          </ul>
        </div>
      `;
    }

    panelBody.innerHTML = bodyHtml;
    panelBody.scrollTop = 0;

    // Show modal
    overlay.classList.add('active');
    overlay.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';

    // Update URL hash smoothly without jump
    if (history.replaceState) {
      history.replaceState(null, null, '#' + cardId);
    }

    // Accessibility focus
    if (closeBtn) closeBtn.focus();
  };

  const closeCardModal = () => {
    if (!overlay) return;
    overlay.classList.remove('active');
    overlay.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    
    // Clear hash without scroll jump
    if (history.replaceState) {
      history.replaceState(null, null, window.location.pathname + window.location.search);
    }

    if (lastFocusedElement && typeof lastFocusedElement.focus === 'function') {
      lastFocusedElement.focus();
    }
  };

  // Expose globally for keyboard / programmatic triggers
  window.openCardModal = openCardModal;
  window.closeCardModal = closeCardModal;

  // Bind Card Click Triggers
  cards.forEach(card => {
    const cardId = card.getAttribute('data-card-id');
    if (!cardId) return;

    // Click whole card
    card.addEventListener('click', (e) => {
      // Don't trigger if user clicked a direct external link inside card
      if (e.target.closest('a') && !e.target.closest('.vcard-overlay-btn')) return;
      openCardModal(cardId);
    });

    // Keyboard support: Enter / Space expands card
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        openCardModal(cardId);
      }
    });

    // Expand button inside footer
    const expandBtn = card.querySelector('.vcard-expand-btn');
    if (expandBtn) {
      expandBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        openCardModal(cardId);
      });
    }
  });

  // Modal Close Triggers
  if (closeBtn) closeBtn.addEventListener('click', closeCardModal);
  if (bottomCloseBtn) bottomCloseBtn.addEventListener('click', closeCardModal);

  // Click outside floating panel (on overlay backdrop)
  if (overlay) {
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) {
        closeCardModal();
      }
    });
  }

  // Keyboard Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && overlay && overlay.classList.contains('active')) {
      closeCardModal();
    }
  });

  // Deep-linking: auto-open if URL has hash matching a topic
  const initialHash = window.location.hash.replace('#', '');
  if (initialHash && topicsMap.has(initialHash)) {
    // Delay slightly to let initial render complete
    setTimeout(() => {
      openCardModal(initialHash);
    }, 150);
  }
}

