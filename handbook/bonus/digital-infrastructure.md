[Handbook](../../README.md) › [Bonus](README.md) ›

# Digital Infrastructure

## Rule

**If the community uses digital infrastructure or public computers, two defaults apply:**

- **Infrastructure runs FreeBSD on ARM hardware.** That covers the servers, storage, firewall, network, and recorders the community owns or runs. ARM uses far less power than the usual x86 (Intel and AMD) machines, which matters when power comes from a small solar and battery system.
- **Computers people sit at run Linux Mint Debian Edition (LMDE).** That covers public computers, the office computer, and any kiosk. Most users only need a web browser, a file manager, and office software such as LibreOffice, and LMDE comes with all three, ready to use. LMDE runs only on x86, so these are the most energy-efficient x86 machines available, such as low-power mini PCs.

Another system or other hardware is used only where a default can't do a particular job (see [When a Default Can't Be Met](#when-a-default-cant-be-met)). **Private devices are not subject to these rules.** A resident's own phone, laptop, tablet, or game console can run anything its owner likes.

**Fiber optic cable links the community's buildings wherever possible.** There is no expectation that the community connects to an outside fiber provider or the main public network. The point is the local network: fiber makes local files, backups, the meeting archive, and camera footage much faster to open, copy, and download between buildings (see [Fiber Optic Network](#fiber-optic-network)).

This page is a bonus. It sits outside the tier triggers. Add it to the charter by a vote when the community first sets up a shared computer, a network, or a server, and add it to your [revision log](../../REVISION_LOG.md).

## What It Covers

| Infrastructure (FreeBSD on ARM) | User computers (LMDE) | Not covered |
|---|---|---|
| Community servers: file storage, backups, the shared calendar, the website | Public computers: a Lodge computer, a homework or library computer | Residents' own phones, laptops, tablets, and desktops |
| The router, firewall, Wi-Fi access points, and fiber network the community runs | The office computer used for bookkeeping, logs, and filings | Visitors' devices |
| The recorder for the security cameras ([Cameras and Surveillance Policy](../part-1-core-chapters/05-people-and-safeguarding/07-cameras-and-surveillance-policy.md)) | A sign-in kiosk | Devices that belong to the internet provider, the bank, or the payment processor |
| The Meeting Hall recorder and archive storage ([Meeting Hall and Meeting Archive](../part-3-site-and-infrastructure/09-shelter-evolution/06-the-meeting-hall-and-meeting-archive.md)) | Any donated computer put into shared use for people to sit at | Sealed appliances with no choice of system (see below) |

**Sealed appliances.** Some devices run built-in software that no one can replace, such as a card reader from the payment processor, a camera's own firmware, or a smart meter. They are allowed. Prefer models that run open firmware, keep them on their own network, and never let them hold community records.

## Why FreeBSD for Infrastructure

- **Small and fast.** A lean system that does a lot on modest, low-power hardware.
- **One complete system from one project.** The core of the system is built and documented together, in the free FreeBSD Handbook, so volunteers learn one system, not a patchwork.
- **ZFS storage built in.** Mirrored disks, snapshots to undo mistakes, checks against silent data damage, and encryption. That suits the meeting archive, camera footage, and members' records.
- **Jails** keep each service, such as the file server, the calendar, and the website, walled off from the others, so a problem in one doesn't spread.
- **The firewall too.** FreeBSD includes the PF firewall, so the router and the servers share one set of skills.
- **Fully supported on ARM.** 64-bit ARM is one of FreeBSD's top-tier platforms, with official installers, packages, and security updates.
- **No license fees,** and open source code that anyone can inspect, with no forced accounts, advertising, or data collection.

## Why ARM Hardware

- **Less power.** A small ARM board often draws only a few watts, while a typical x86 desktop draws tens of watts, and more under load. Machines that run all day, such as the server, the firewall, and the camera recorder, save the most.
- **Smaller solar and battery systems.** As with LED lighting, lower loads mean smaller panels and batteries, and smaller wind and heat-store sizing ([Chapter 14](../part-3-site-and-infrastructure/14-lighting-standard.md), [Chapter 16](../part-3-site-and-infrastructure/16-wind-power-and-wind-safety.md)).
- **Less heat.** The network cabinet stays cooler in summer, and many boards need no fan at all.
- **Small and quiet,** easy to mount in the network cabinet.
- **Measure it.** Use a plug-in power meter, and log each device's watts on the network map.

**RISC-V is for light services only, for now.** FreeBSD runs on RISC-V, but as a less mature platform: security updates, releases, and packages aren't guaranteed the way they are on ARM, and fewer boards are supported. A RISC-V board may run a light, non-critical service. It does not run the firewall, archive storage, or backups until FreeBSD supports RISC-V fully.

## Why Linux Mint Debian Edition for Users

- **Ready to use.** Firefox, a file manager, and LibreOffice come installed, which is all most users need.
- **Familiar.** The desktop works the way people who have used Windows expect: a start menu, a taskbar, and windows.
- **Built on Debian,** a stable, long-supported base, without depending on any one company.
- **Easy to look after.** The Update Manager can install updates automatically, and the login settings can offer a guest session for public computers.
- **No license fees,** no forced accounts, advertising, or data collection, and a large community for help.

## Choosing a System

| Job | System | Hardware |
|---|---|---|
| Public and office computers | LMDE, with Firefox, the file manager, and LibreOffice | A low-power x86 mini PC, wired to the network |
| Servers (files, calendar, website) | FreeBSD, with each service in its own jail | An ARM server board. A RISC-V board only for light, non-critical services. |
| Storage for backups and the archive | FreeBSD with ZFS on mirrored disks | An ARM board with plenty of memory and connections for two or more drives |
| Router and firewall | FreeBSD with its built-in PF firewall | An ARM board with two or more network ports, or fiber ports |
| Wi-Fi access points | Open firmware, usually OpenWrt (Linux), since FreeBSD doesn't run on most access points | ARM-based access points |
| Camera recorder | FreeBSD, if the chosen open camera-recording software runs on it. Otherwise Linux (see below). | An ARM board with storage sized for the retention limit |

**Point-and-click firewalls run on x86.** OPNsense and pfSense, both built on FreeBSD, let volunteers manage the firewall from a web page instead of a settings file. Their free editions run mainly on x86, so choosing one is a recorded exception to the hardware default.

**Software for everyday users:** Firefox, the file manager, LibreOffice for documents and spreadsheets (the logs and sheets in [Appendix D](../appendices/appendix-d-logs-sheets-and-reports/README.md)), a PDF reader, and open bookkeeping software. Ask the accountant which file formats they accept before choosing.

**Check the hardware first.**

- **ARM boards:** start FreeBSD from the ready-made image FreeBSD publishes for many ARM boards, and check that the network, storage, and any fiber ports work. Support for the newest boards often lags, so test one before buying more.
- **User computers:** start LMDE from a live USB stick, without installing, and check that the screen, network, sound, and printer work.
- A wired connection (copper inside the building, fiber between buildings) works best, which is one more reason public and office computers are wired mini PCs.

**Use a solid-state drive, not a memory card,** for the system and data on any server, firewall, or recorder. Memory cards wear out quickly under constant writing.

**Stay on supported releases.** Each FreeBSD and LMDE release gets security updates for a set period. Note the end dates on the [compliance calendar](../appendices/appendix-d-logs-sheets-and-reports/d09-compliance-calendar.md), and plan each upgrade before its date.

## When a Default Can't Be Met

**Another system.** For that one job only:

- **Linux or another BSD instead of FreeBSD** for infrastructure, when the device can't run FreeBSD (such as most Wi-Fi access points), the hardware isn't supported and supported hardware isn't affordable yet, or the software the job needs doesn't run on FreeBSD (such as some camera-recording software)
- **Another Linux system instead of LMDE** for a user computer, when LMDE can't do that job or doesn't support the hardware

**Other hardware.** An x86 machine may run infrastructure instead of ARM, for that one job only, when:

- **No ARM hardware can do the job,** such as a point-and-click firewall the volunteers need
- **A donated x86 computer works well.** Using it avoids waste and cost. Replace it with ARM hardware when it wears out, or sooner if the power saved would pay for the replacement.

**When FreeBSD and ARM can't both be met,** keep FreeBSD and choose the most energy-efficient x86 machine that runs it, such as a low-power mini PC.

For each exception, write down the job, the system or hardware used instead, and why, on the network map. Review the list every year, and move the job back to the defaults when it can be. Software made only for Windows or macOS is a different case (see [When a Required Program Won't Run](#when-a-required-program-wont-run)).

## Running It Safely

**People**

- [ ] **Two administrators** for every system, so no one person holds the only access. This is the two-person rule from the [Introduction](../part-1-core-chapters/01-introduction.md).
- [ ] Administrator passwords kept in a password manager or a sealed envelope, held by both administrators. Change them when an administrator leaves.
- [ ] Each person who uses the office computer or servers has their own account. No shared logins.

**Updates and backups**

- [ ] **Security updates installed automatically,** on FreeBSD (scheduled freebsd-update and pkg) and on LMDE (the Update Manager's automatic updates), and checked monthly
- [ ] **ZFS snapshots** taken on a schedule, so a deleted or damaged file can be brought back quickly
- [ ] **Backups:** three copies, on two kinds of storage, with one copy off site. Snapshots alone are not a backup. Test a restore each season.
- [ ] Camera footage and meeting recordings never share storage or administrators, as the camera policy and the meeting recording policy already require
- [ ] Disk encryption (ZFS encryption or GELI on FreeBSD, or full-disk encryption chosen when installing LMDE) on any computer or drive that holds members' records, complaints, health details, or footage

**Power**

- [ ] Every always-on device (the server, firewall, switches, and camera recorder) on a battery backup that lasts long enough to shut it down cleanly in a power cut
- [ ] Each device's power use measured and logged on the network map

**Networks**

- [ ] **A separate guest network** for residents' and visitors' private devices. Private devices never join the network that the office computer and servers use.
- [ ] **A separate network for cameras and sealed appliances**
- [ ] The router's default password changed on day one, and its remote management turned off

**Public computers**

- [ ] Set in an open, visible spot, never in a private room ([Safeguarding](../part-1-core-chapters/05-people-and-safeguarding/02-safeguarding-children-and-vulnerable-adults.md))
- [ ] A guest session that is wiped at every logout, so no one's browsing, files, or passwords are left behind. The administrators turn it on in LMDE's login settings and test it.
- [ ] No community records stored on a public computer
- [ ] Children use public computers under the same supervision rules as any other shared space. Use family-safe filtering where the law or the group requires it.
- [ ] The community does not monitor what people do on public computers beyond what the law requires. Keep logs short and delete them on a schedule.

## Fiber Optic Network

**Rule:** cable between buildings is **fiber optic wherever possible.** Copper network cable is fine inside a building, and Wi-Fi is fine for private devices.

**Why fiber between buildings**

- **Speed for local files.** Files on the community server, backups, meeting recordings, and camera footage move between buildings at full speed, whatever the outside internet connection is like.
- **It works without the internet.** The local network keeps running during an outage, or if the community has only a slow outside connection, or none.
- **No lightning or electrical path.** Fiber is glass, not metal, so it cannot carry a lightning surge or stray current from one building to another. Copper cable run between buildings can, and it can destroy the equipment at both ends.
- **Long runs.** Copper network cable is limited to about 328 ft (100 m). Fiber runs much farther, so the farthest cabin or the Meeting Hall can be reached in one length.
- **It lasts.** Fiber does not corrode, and the same cable can carry faster equipment later.
- **No expectation of joining the main infrastructure.** If a fiber internet provider reaches the area, the community may connect, but it is never required. The local network is worth building on its own.

**Laying it**

- [ ] **Conduit first.** Lay conduit with a pull string in every utility trench and road sleeve as it is dug ([Utility Trenches and Access Pits](../part-3-site-and-infrastructure/10-water-plumbing-and-septic/03-utility-trenches-and-access-pits.md)), even before there is fiber to pull. Digging once costs far less than digging twice.
- [ ] **Keep it in its own conduit,** apart from power, as the electrical code requires
- [ ] **Outdoor-rated cable** made for conduit or direct burial, with a moisture barrier
- [ ] **All-dielectric (no metal) cable** where possible, so it carries no lightning. If armored cable with metal is used, bond the armor to ground as the code requires.
- [ ] **Single-mode fiber** for runs between buildings, since it covers the longest distances and suits future equipment. Ask the installer to confirm.
- [ ] **Spare strands:** pull more strands than you need now (for example, 12), so a broken strand or a new building doesn't mean a new cable
- [ ] **Pre-terminated cable or a trained installer.** Joining and finishing fiber ends takes special tools, so buy cable with the ends already fitted, or pay someone to do it.
- [ ] **Never bend it sharply.** Follow the maker's minimum bend radius, and use pull boxes on long or bending runs.
- [ ] **Warning tape and a tracer** above buried runs, because fiber cannot be found with a metal detector
- [ ] **A star layout:** every building runs back to one network cabinet in a noncombustible, lockable building, next to the community server
- [ ] **A map** of every run, conduit, and strand, kept with the network passwords by both administrators

**Equipment**

- A network switch with fiber ports, or a small converter, at each end of every fiber run
- Copper cable or Wi-Fi from that switch to the computers inside each building
- Cameras that take power through their network cable still need copper for the last stretch, or a power supply at the camera, with fiber back to the recorder

**Safety**

- [ ] **Never look into the end of a fiber or a fiber port.** The light is often invisible and can damage eyes.
- [ ] Wear safety glasses when cutting or finishing fiber, and pick up glass scraps with tape. Dispose of them in a sealed container, away from food and children.
- [ ] Call the local utility locating service before digging, and check the community's own fiber map

## When a Required Program Won't Run

Sometimes a bank, a tax office, or an accountant uses software made only for Windows or macOS. Work through these steps in order:

1. **Use the web version.** Most banking, tax filing, and payment services work in Firefox on LMDE.
2. **Use the professional's own systems.** Send the accountant or attorney the files, and let them run their software.
3. **Ask for another format,** such as a spreadsheet or PDF instead of a program file.
4. **Only if all three fail,** the board may approve a narrow written exception for that one task. Record the reason and the date in the revision log, keep the machine off the community network, store no community records on it, and review the exception every year.

## Tier Fit

- **Tier 0:** no community computers are needed. Private phones and laptops are fine. If the group takes in a shared or donated computer, it runs LMDE from the start, after the hardware check.
- **Tier 1:** one office computer, a low-power x86 mini PC running LMDE with Firefox and LibreOffice, for the logs, budget, and filings, with two administrators and an off-site backup
- **Tier 2:** a community router and firewall (FreeBSD with PF, on an ARM board) with a guest network, and a camera recorder on its own network with off-site storage. Lay conduit with a pull string in every utility trench and road sleeve as it is dug.
- **Tier 3:** a small ARM server running FreeBSD with ZFS for files, the shared calendar, and backups, the Meeting Hall recorder and archive storage, and a public computer in the Lodge. Pull fiber from the network cabinet to the Lodge, the Meeting Hall, and the camera recorder.
- **Tier 4:** fiber to every building that needs the network, and a yearly review of systems, updates, backups, accounts, the fiber map, power use, any jobs not yet on the default systems or hardware, and any exceptions

## Common Failures

- One volunteer who knows every password, then leaves
- A donated computer put into use with its old system and the last owner's files still on it
- Updates turned off "until later"
- Backups that were never tested, or kept only on site
- Residents' private devices on the same network as the office computer and the camera recorder
- Members' records saved on a public computer
- The router still using its default password
- Asking residents to change what runs on their own devices. The rule covers community systems only.
- Accepting a donated computer without testing it with the system it will run
- Each volunteer installing a different favorite system, so no one can look after them all
- Letting a FreeBSD or LMDE release run past the end of its security updates
- Buying x86 out of habit when an ARM board would do the job
- Running a server from a memory card until it wears out
- Buying several ARM boards before testing that FreeBSD runs well on one
- Running the firewall, archive storage, or backups on RISC-V before FreeBSD supports it fully
- Copper network cable run between buildings, then destroyed by a lightning strike
- Burying fiber without conduit, or digging a trench without laying spare conduit
- No spare strands, so one damaged strand means a new cable
- No map of the fiber runs, so a digger cuts one

## Money Tie-In

- Track hardware, storage, internet, and backup costs in the [expense log](../appendices/appendix-d-logs-sheets-and-reports/d06-expense-log.md)
- Accept donated hardware, but wipe it and install a fresh system before use
- ARM boards usually cost less to buy and to run. Log the power saved next to the LED savings in the annual report ([Chapter 14](../part-3-site-and-infrastructure/14-lighting-standard.md))
- Pay a local technician for setup if no member has the skills, and have them train the two administrators
- Most of the cost of fiber is digging and conduit, not the cable. Lay conduit during trench and road work, and pull fiber later as funds allow ([capital plan](../appendices/appendix-d-logs-sheets-and-reports/d20-capital-plan-and-build-order.md))

> Data protection, privacy, children's online safety, and record-keeping rules differ by location. This handbook gives no legal advice, so check what applies to the records and computers you keep, and ask an attorney before collecting members' personal data.

<!-- nav: generated by scripts/nav.py, do not edit below -->

---

← **Previous:** [Bonus](README.md)
