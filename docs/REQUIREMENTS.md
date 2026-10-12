# Multi-Vendor Marketplace – Requirements & Build Plan

Oct 12, 2026 · BI Team

> Source of truth for this project. Requirement IDs (e.g. FR-CAT-01, SEC-05) are
> referenced in code comments, commits and tests.

## Executive Summary

We are building a multi-vendor marketplace for Pakistan where independent vendors sell
both products and services, and the platform earns a commission on every sale. The
platform admin controls the whole site, and each vendor manages only its own store,
team, listings and orders.

| Decision | Choice |
|---|---|
| Business model | Multi-vendor marketplace; platform earns a commission per sale |
| What is sold | Physical products and services |
| Customization | Vendors define their own options (size, color, material, packages) and custom details per listing |
| Control | Platform admin controls everything; vendors control only their own side |
| Money flow | Platform collects all payments, keeps commission, pays vendors on a schedule |
| Tech stack | Python (Django), PostgreSQL, Tailwind CSS |
| Launch market | Pakistan, PKR, English, mobile-friendly website |

Requirements are numbered (e.g. FR-CAT-01) so each one can be referenced in design,
build and testing. Defaults proposed during planning are listed under Assumptions &
Open Items.

## User Roles & Permissions

The platform has five roles across two admin levels: the platform admin controls the
marketplace, and each vendor runs its own team of owner, managers and staff.

| Capability | Platform Admin | Vendor Owner | Vendor Manager | Vendor Staff | Customer |
|---|---|---|---|---|---|
| Approve, suspend and verify vendors | Yes | | | | |
| Manage categories and commission rates | Yes | | | | |
| Moderate listings (approve or reject) | Yes | | | | |
| Run site-wide promotions | Yes | | | | |
| Resolve disputes, approve payouts | Yes | | | | |
| Manage own store profile and team members | Yes | Yes | | | |
| View own earnings and payouts | Yes | Yes | | | |
| Create and edit own listings, options, prices, stock | Yes | Yes | Yes | | |
| Create own sales, discounts and coupons | Yes | Yes | Yes | | |
| Manage own service availability and bookings | Yes | Yes | Yes | Yes | |
| Process own orders (confirm, ship, deliver) | Yes | Yes | Yes | Yes | |
| Browse, buy, book, review, raise disputes | | | | | Yes |

- **FR-ROLE-01:** A vendor can have multiple team members, each with exactly one role.
- **FR-ROLE-02:** A vendor's team sees only that vendor's data; no vendor can see another
  vendor's listings, orders, customers or earnings.
- **FR-ROLE-03:** Vendors use a dedicated Vendor Portal; the platform admin uses the Admin Panel.

## Catalog: Products, Services, Options & Discounts

Every item sold is a listing of type Product or Service, and vendors fully control its
options, pricing, stock and discounts.

| ID | Requirement | Details |
|---|---|---|
| FR-CAT-01 | Listings can be products or services | Same catalog, search and checkout for both |
| FR-CAT-02 | Platform-controlled categories | Nested categories managed by the platform admin only |
| FR-CAT-03 | Vendor-defined options per listing | Vendor creates any option types (Color, Size, Material, Package) and their values; not limited to a fixed list |
| FR-CAT-04 | Customer selects options before buying | e.g. Red / Large, or Premium package |
| FR-CAT-05 | Optional price per option combination | Vendor decides if a combination changes the price; otherwise the base price applies |
| FR-CAT-06 | Stock tracked per option combination | e.g. Red / Large has its own quantity; out-of-stock combinations cannot be ordered |
| FR-CAT-07 | Vendor-defined custom details | Free key-value specifications per listing, e.g. Fabric: Cotton, Warranty: 1 year |
| FR-CAT-08 | Multiple images per listing | Ordered gallery; optional image per option value (e.g. per color) |
| FR-CAT-09 | Listing moderation | Draft, Pending Review, Published, Rejected (with reason); only published listings of approved vendors are visible |
| FR-CAT-10 | Vendor sales and discounts | Percentage or fixed amount; on a whole listing, specific option combinations, or several listings; optional start and end dates that switch automatically |
| FR-CAT-11 | Sale price display | Original price shown struck through beside the sale price |
| FR-CAT-12 | Coupon codes | Vendor coupons for own listings; platform coupons site-wide; usage limits and expiry |
| FR-CAT-13 | SKUs unique across platform | Auto-prefixed with the vendor code |

Services add these requirements:

| ID | Requirement | Details |
|---|---|---|
| FR-SVC-01 | Delivery mode chosen by vendor per service | Booking (date and time slot) or Order and deliver later |
| FR-SVC-02 | Service packages | Options such as Basic, Standard, Premium, each with its own price and delivery time |
| FR-SVC-03 | Availability calendar for booking services | Working hours, slot length, slots per time (capacity), blocked dates |
| FR-SVC-04 | Customer books an available slot | Slot is held during checkout and confirmed on order |
| FR-SVC-05 | Delivery time for order-based services | Vendor sets expected delivery days per package |

## Cart, Checkout, Orders & Payments

A customer checks out once, and the order is split into one sub-order per vendor; the
platform collects the money and pays each vendor its earnings after commission.

| ID | Requirement | Details |
|---|---|---|
| FR-ORD-01 | Multi-vendor cart | Products and services from several vendors in one cart, grouped by vendor |
| FR-ORD-02 | Customer instructions | Free-text notes to the vendor, per item, at order time |
| FR-ORD-03 | Order splitting | One customer order becomes one vendor order per vendor, each with its own status and tracking |
| FR-ORD-04 | Price snapshot | Order lines store name, options, SKU and price paid, so later edits never change past orders |
| FR-ORD-05 | Stock reservation | Stock and booking slots are reserved at checkout and released if payment fails or the order is cancelled |
| FR-ORD-06 | Vendor order statuses | Pending, Confirmed, Shipped / In progress, Delivered / Completed, Cancelled, Returned |
| FR-PAY-01 | Payment methods at launch | Cash on Delivery plus one online gateway (cards and mobile wallets such as JazzCash, Easypaisa) |
| FR-PAY-02 | Platform collects all payments | Gateway pays the platform; vendors never receive customer payments directly |
| FR-PAY-03 | Commission per vendor | Percentage set per vendor by the platform admin, snapshotted on each vendor order |
| FR-PAY-04 | Commission on discounted price | Calculated on the amount the customer actually paid for items; shipping passes through to the vendor |
| FR-PAY-05 | Vendor payouts | Scheduled payouts (e.g. weekly) of delivered, non-disputed orders, approved by the platform admin |
| FR-PAY-06 | Earnings statement | Vendors see sales, commission, refunds and payouts per period |

The gateway choice is open: availability of split payments and merchant fees for
Pakistani gateways must be confirmed before Phase 6.

## Fulfillment, Returns, Reviews & Notifications

Vendors fulfil their own orders, while the platform sets minimum policies and resolves
disputes.

| ID | Requirement | Details |
|---|---|---|
| FR-FUL-01 | Vendors ship their own products | Vendor enters courier and tracking number; courier integration later |
| FR-FUL-02 | Vendor shipping rates | Each vendor sets its own rates (flat or by city) |
| FR-FUL-03 | Service fulfilment | Booking services are marked Completed after the appointment; order-based services after delivery |
| FR-FUL-04 | Customer order tracking | Customer sees status and tracking per vendor shipment |
| FR-RET-01 | Cancellation | Customer can cancel before the vendor ships or before the booking's cancellation cut-off |
| FR-RET-02 | Returns and refunds | Handled per vendor within a platform-wide minimum policy |
| FR-RET-03 | Disputes | Customer raises a ticket; platform admin mediates and decides |
| FR-REV-01 | Reviews and ratings | Only verified buyers can rate listings and vendors; vendors can reply |
| FR-NOT-01 | Email notifications at launch | Order placed, confirmed, shipped, delivered, booking reminders, payouts |
| FR-NOT-02 | SMS and WhatsApp updates | Later phase |

## Security Requirements

All Must-have checks ship at launch; Later checks are scheduled as the platform grows.

| ID | Area | Check | Priority |
|---|---|---|---|
| SEC-01 | Accounts | Strong password rules; passwords hashed, never readable | Must-have |
| SEC-02 | Accounts | Email and phone OTP verification at sign-up | Must-have |
| SEC-03 | Accounts | Login attempt limits, temporary lockout, CAPTCHA | Must-have |
| SEC-04 | Accounts | Two-factor authentication for platform admins and vendor owners | Must-have |
| SEC-05 | Access | Strict vendor data isolation in every query and view | Must-have |
| SEC-06 | Access | Role-based permissions inside each vendor team | Must-have |
| SEC-07 | Access | Customers see only their own orders, bookings and addresses | Must-have |
| SEC-08 | Vendors | Vendor approval with CNIC, business and contact verification | Must-have |
| SEC-09 | Vendors | Bank account verification before payouts | Must-have |
| SEC-10 | Payments | Card data handled only by the gateway, never stored | Must-have |
| SEC-11 | Payments | Signed gateway webhooks verify every payment confirmation | Must-have |
| SEC-12 | Payments | Payout approval workflow with audit trail | Must-have |
| SEC-13 | Fraud | Phone verification for COD and limits on unconfirmed orders | Must-have |
| SEC-14 | App | HTTPS everywhere; protection against SQL injection, XSS, CSRF | Must-have |
| SEC-15 | App | File upload checks: allowed types, size limits, image re-processing | Must-have |
| SEC-16 | App | Rate limiting on login, OTP, checkout and search | Must-have |
| SEC-17 | Data | Encryption of CNIC and bank details at rest | Must-have |
| SEC-18 | Data | Daily automated backups with tested restore | Must-have |
| SEC-19 | Data | Vendors see only the customer data needed to fulfil an order | Must-have |
| SEC-20 | Monitoring | Audit log of admin and vendor actions | Must-have |
| SEC-21 | Monitoring | Error and security alerting | Must-have |
| SEC-22 | Legal | Terms of service, vendor agreement, privacy, refund policies | Must-have |
| SEC-23 | Accounts | Optional 2FA for customers | Later |
| SEC-24 | Fraud | Blocklist for repeat fraudulent phones, emails, addresses | Later |
| SEC-25 | App | Regular dependency updates and security scans | Later |
| SEC-26 | Legal | Compliance review with local law (e.g. PECA) before scaling | Later |

Policies and the vendor agreement should be reviewed by a lawyer before launch.

## Non-Functional Requirements

The site must be fast on mobile, easy to grow, and measurable from day one. Targets
below are proposals to confirm.

| ID | Area | Requirement |
|---|---|---|
| NFR-01 | Devices | Mobile-first responsive design; usable on low-end Android phones |
| NFR-02 | Performance | Proposed target: key pages load in under 3 seconds on a mobile 4G connection |
| NFR-03 | Scalability | Architecture supports adding mobile apps later through an API layer |
| NFR-04 | Localization | English and PKR at launch; time zone Asia/Karachi; structure ready for Urdu later |
| NFR-05 | SEO | Clean URLs, page titles and descriptions, sitemap, structured product data |
| NFR-06 | Analytics | GA4 e-commerce events; PostgreSQL data exported to BigQuery for Looker Studio dashboards (platform and per vendor) |
| NFR-07 | Reliability | Daily backups; error monitoring; staging environment before production |
| NFR-08 | Maintainability | Automated tests for checkout, order splitting, commission and permissions |
| NFR-09 | Data quality | Timestamps on every table for incremental ETL; price and status snapshots for accurate reporting |
| NFR-10 | Future AI | Clean listing and order data to support recommendations and a support agent later |

## Technology Stack & Architecture

One Django application on PostgreSQL serves three front ends: the customer Storefront,
the Vendor Portal and the Admin Panel.

```
 Customers            Vendor teams              Platform admin
     |                     |                          |
 Storefront           Vendor Portal              Admin Panel
 (browse, buy,        (own listings,             (approvals, payouts,
  book, track)         orders, earnings)          disputes)
     \                     |                          /
      +-------------- Django application ------------+
      | accounts | vendors | catalog | bookings      |
      | promotions | cart and orders | payments      |
      | reviews and support                          |
      +----------------------------------------------+
        |            |           |          |          |
   PostgreSQL   Media files   Payments   Email/SMS   BigQuery
   (core data)  (images)      (cards,    (notifs)    (Looker Studio BI)
                              wallets)
```

Every request passes through the same permission layer, which is what keeps each
vendor's data isolated.

| Layer | Choice | Why |
|---|---|---|
| Backend | Python 3.12+, Django 5.2 LTS | Matches team skills; built-in admin, authentication and security protections |
| Database | PostgreSQL | Reliable transactions, constraints and JSON support for flexible options |
| Frontend | Django templates, Tailwind CSS, htmx | Fast to build and mobile-friendly; an API layer is added later for mobile apps |
| Background jobs | Celery with Redis | Emails, sale start and end, slot release, payouts, ETL |
| Media storage | S3-compatible object storage | Keeps images off the app server |
| Hosting | Managed platform or VPS, with staging and production | Safe testing before release |
| Payments | Local gateway plus Cash on Delivery | Fits the Pakistan market |
| Notifications | Transactional email provider; SMS provider later | Order and booking updates |
| Analytics | GA4, BigQuery, Looker Studio | Platform and vendor dashboards |

## Data Model

The database has about 25 core tables in PostgreSQL, grouped by Django app; every table
carries created and updated timestamps.

| App | Entity | Purpose | Key relationships |
|---|---|---|---|
| accounts | User | Customers, vendor team members, platform staff | Has addresses, orders, memberships |
| accounts | Address | Saved customer addresses | Belongs to User |
| vendors | Vendor | Store profile, status, commission rate, verification | Has members, listings, vendor orders, payouts |
| vendors | VendorMember | Links a user to a vendor with a role | User + Vendor (unique pair) |
| vendors | VendorVerification | CNIC, business documents, bank account (encrypted) | Belongs to Vendor |
| vendors | ShippingRate | Vendor shipping rates, flat or by city | Belongs to Vendor |
| catalog | Category | Platform-managed nested categories | Self-referencing parent |
| catalog | Listing | A product or service (type field), status, description | Belongs to Vendor and Category |
| catalog | ListingAttribute | Custom key-value details | Belongs to Listing |
| catalog | OptionType | Vendor-defined option, e.g. Size | Belongs to Listing |
| catalog | OptionValue | A value, e.g. Large | Belongs to OptionType |
| catalog | Variant | One option combination with SKU, optional price, stock | Belongs to Listing; links many OptionValues |
| catalog | ListingImage | Gallery images | Belongs to Listing; optional OptionValue |
| bookings | AvailabilityRule | Working hours, slot length, capacity | Belongs to service Listing |
| bookings | BlockedDate | Days off and holidays | Belongs to service Listing |
| bookings | Booking | A reserved slot for an order line | Belongs to OrderItem |
| promotions | Sale | Scheduled percentage or fixed discount | Belongs to Vendor; applies to Listings or Variants |
| promotions | Coupon | Code-based discount, limits, expiry | Belongs to Vendor or platform |
| cart | Cart, CartItem | Items before checkout, with customer instructions | Belongs to User or session |
| orders | Order | Customer checkout, payment, shipping snapshot, totals | Has vendor orders |
| orders | VendorOrder | One vendor's part: status, tracking, commission, earnings | Belongs to Order and Vendor |
| orders | OrderItem | Line snapshot: name, options, SKU, price, quantity, instructions | Belongs to VendorOrder |
| payments | Payment, Refund | Gateway transactions and refunds | Belongs to Order |
| payments | Payout | Payments to vendors per period | Belongs to Vendor; groups VendorOrders |
| reviews | Review | Verified-buyer rating, text, vendor reply | Belongs to OrderItem |
| support | Ticket, TicketMessage | Disputes and support conversations | Belongs to Order or VendorOrder |
| core | AuditLog, Notification | Who did what; messages sent | Linked to any record |

## Project Structure

The codebase is one Django project split into focused apps, one per business area, so
each can be built and tested on its own.

```
marketplace/
├── config/            # settings, URLs, shared base models
├── core/              # audit log, notifications, shared utilities
├── accounts/          # users, addresses, login, OTP, 2FA
├── vendors/           # vendors, team members, verification, shipping rates
├── catalog/           # categories, listings, options, variants, images
├── bookings/          # service availability and slot bookings
├── promotions/        # sales and coupons
├── cart/              # cart and checkout
├── orders/            # orders, vendor orders, order items
├── payments/          # gateway, refunds, payouts
├── reviews/           # ratings and vendor replies
├── support/           # disputes and tickets
├── storefront/        # customer-facing pages
├── vendor_portal/     # vendor dashboard pages
├── analytics/         # BigQuery export jobs
├── templates/         # HTML templates (Tailwind CSS)
├── static/            # CSS, JS, icons
├── tests/             # automated tests
├── requirements.txt
├── .env               # secrets, never committed
└── manage.py
```

## Build Roadmap

The build runs in nine phases, each ending with a working, testable result; dates will
be set once team size and hours are known.

1. **Foundation:** project setup, all core tables, admin panel, vendor and listing
   approval. *Done when* the admin can create a vendor and a listing with options and variants.
2. **Accounts & security base:** sign-up, login, OTP, 2FA for admins and vendor owners,
   rate limiting. *Done when* SEC-01 to SEC-07 pass testing.
3. **Storefront:** home, category pages, search and filters, listing page with option
   selection, vendor store pages. *Done when* customers can browse and pick a variant.
4. **Cart & checkout:** multi-vendor cart, instructions, order splitting, stock
   reservation, COD. *Done when* a two-vendor COD order splits correctly.
5. **Vendor portal:** vendor sign-up and verification, dashboard, listings, options,
   stock, sales and coupons, order processing, team management. *Done when* a vendor runs
   its store without admin help.
6. **Services & bookings:** availability calendars, slot booking, order-based services.
   *Done when* a customer books and completes a service.
7. **Payments & payouts:** online gateway, webhooks, refunds, commission ledger, payouts.
   *Done when* a paid order flows through to a vendor payout.
8. **After-sales & launch:** reviews, disputes, email notifications, policies,
   deployment, backups, monitoring. *Done when* the launch security checklist passes.
9. **Analytics & AI:** BigQuery export, Looker Studio dashboards, recommendations,
   support agent.

## Assumptions & Open Items

These defaults were proposed during planning and are treated as approved unless changed here.

| Area | Assumed default |
|---|---|
| Platform revenue | Commission per sale, adjustable per vendor; vendor subscription plans possible later |
| Payment collection | Platform collects all payments and pays vendors on a schedule |
| Shipping | Vendors ship their own orders and set their own rates |
| Returns | Per vendor, within a platform-wide minimum policy |
| Disputes | Resolved by the platform admin through tickets |
| Customer instructions | Text only; no file attachments |
| Guest checkout | Allowed, with phone verification |
| Language and currency | English, PKR |
| Geography | Pakistan only |
| Platform | Responsive website first; mobile apps later |

Open questions to answer before or during the build:

- [ ] Which product and service categories will launch first?
- [ ] Which online payment gateway, and does it support split payments?
- [ ] Default commission rate, and payout frequency (weekly or monthly)?
- [ ] Minimum return and refund window for all vendors?
- [ ] Should customers attach files (reference images, designs) to instructions?
- [ ] Marketplace name and domain?
- [ ] Team size, budget and target launch date?
