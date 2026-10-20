[Handbook](../../README.md) › [Bonus](README.md) ›

# Digital Infrastructure: Linux, BSD, and Fiber

## Rule

**If the community uses digital infrastructure or public computers, they run Linux or one of the BSDs.** That covers every computer, server, and network device the community owns, runs, or offers for shared use. **Private devices are not subject to this rule.** A resident's own phone, laptop, tablet, or game console can run anything its owner likes.

**Fiber optic cable links the community's buildings wherever possible.** There is no expectation that the community connects to an outside fiber provider or the main public network. The point is the local network: fiber makes local files, backups, the meeting archive, and camera footage much faster to open, copy, and download between buildings (see [Fiber Optic Network](#fiber-optic-network)).

This page is a bonus. It sits outside the tier triggers. Add it to the charter by a vote when the community first sets up a shared computer, a network, or a server, and add it to your [revision log](../../REVISION_LOG.md).

## What It Covers

| Covered (Linux or BSD) | Not covered |
|---|---|
| Community servers: file storage, backups, the shared calendar, the website | Residents' own phones, laptops, tablets, and desktops |
| The router, firewall, Wi-Fi access points, and fiber network the community runs | Visitors' devices |
| The recorder for the security cameras ([Cameras and Surveillance Policy](../part-1-core-chapters/05-people-and-safeguarding/07-cameras-and-surveillance-policy.md)) | Devices that belong to the internet provider, the bank, or the payment processor |
| The Meeting Hall recorder and archive storage ([Meeting Hall and Meeting Archive](../part-3-site-and-infrastructure/09-shelter-evolution/06-the-meeting-hall-and-meeting-archive.md)) | Sealed appliances with no choice of system (see below) |
| The office computer used for bookkeeping, logs, and filings | |
| Public computers: a Lodge computer, a homework or library computer, a sign-in kiosk | |
| Any donated computer, once it is put into shared use | |

**Sealed appliances.** Some devices run built-in software that no one can replace, such as a card reader from the payment processor, a camera's own firmware, or a smart meter. They are allowed. Prefer models that run Linux or open firmware, keep them on their own network, and never let them hold community records.

## Why Linux and the BSDs

- **No license fees.** Money goes to the reserve, not to software renewals ([Chapter 8](../part-2-market-engine/08-money-rules/README.md)).
- **They run well on old and donated hardware,** which suits a community that grows only as funds allow.
- **Long support and steady updates,** so a system set up at Tier 1 can still be safe at Tier 4.
- **Open source code** that anyone can inspect. That matters for systems that hold camera footage, the meeting archive, and members' private records.
- **No forced accounts, advertising, or data collection** built into the system.
- **No single vendor to depend on.** Many volunteers, and many local technicians, can maintain them.

## Choosing a System

These are common, well-supported starting points, not the only good choices. Pick one per job and stay with it, so the volunteers who maintain it don't have to learn several.

| Job | Common choices |
|---|---|
| Public and office computers | A desktop Linux system built for ease of use, such as Linux Mint, Ubuntu, Debian, or Fedora |
| Servers (files, calendar, backups, archive) | Debian, Ubuntu LTS, or FreeBSD |
| Router and firewall | OpenWrt (Linux), or OPNsense or pfSense (FreeBSD) |
| Firewall where security matters most | OpenBSD |
| Storage for backups and the archive | A Linux or FreeBSD server with mirrored disks |
| Camera recorder | A Linux server running open camera-recording software |

**Software that works on all of these:** a web browser such as Firefox, LibreOffice for documents and spreadsheets (the logs and sheets in [Appendix D](../appendices/appendix-d-logs-sheets-and-reports/README.md)), and open bookkeeping software. Ask the accountant which file formats they accept before choosing.

**Before you choose,** check that the system still gets security updates and that at least two members can look after it.

## Running It Safely

**People**

- [ ] **Two administrators** for every system, so no one person holds the only access. This is the two-person rule from the [Introduction](../part-1-core-chapters/01-introduction.md).
- [ ] Administrator passwords kept in a password manager or a sealed envelope, held by both administrators. Change them when an administrator leaves.
- [ ] Each person who uses the office computer or servers has their own account. No shared logins.

**Updates and backups**

- [ ] **Security updates turned on to install automatically,** and checked monthly
- [ ] **Backups:** three copies, on two kinds of storage, with one copy off site. Test a restore each season.
- [ ] Camera footage and meeting recordings never share storage or administrators, as the camera policy and the meeting recording policy already require
- [ ] Disk encryption on any computer or drive that holds members' records, complaints, health details, or footage

**Networks**

- [ ] **A separate guest network** for residents' and visitors' private devices. Private devices never join the network that the office computer and servers use.
- [ ] **A separate network for cameras and sealed appliances**
- [ ] The router's default password changed on day one, and its remote management turned off

**Public computers**

- [ ] Set in an open, visible spot, never in a private room ([Safeguarding](../part-1-core-chapters/05-people-and-safeguarding/02-safeguarding-children-and-vulnerable-adults.md))
- [ ] A guest account that wipes itself at logout, so no one's browsing, files, or passwords are left behind
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

1. **Use the web version.** Most banking, tax filing, and payment services work in a browser on Linux or BSD.
2. **Use the professional's own systems.** Send the accountant or attorney the files, and let them run their software.
3. **Ask for another format,** such as a spreadsheet or PDF instead of a program file.
4. **Only if all three fail,** the board may approve a narrow written exception for that one task. Record the reason and the date in the revision log, keep the machine off the community network, store no community records on it, and review the exception every year.

## Tier Fit

- **Tier 0:** no community computers are needed. Private phones and laptops are fine. If the group takes in a shared or donated computer, it runs Linux or BSD from the start.
- **Tier 1:** one office computer for the logs, budget, and filings, with two administrators and an off-site backup
- **Tier 2:** a community router and firewall with a guest network, and a camera recorder on its own network with off-site storage. Lay conduit with a pull string in every utility trench and road sleeve as it is dug.
- **Tier 3:** a small server for files, the shared calendar, and backups, the Meeting Hall recorder and archive storage, and a public computer in the Lodge. Pull fiber from the network cabinet to the Lodge, the Meeting Hall, and the camera recorder.
- **Tier 4:** fiber to every building that needs the network, and a yearly review of systems, updates, backups, accounts, the fiber map, and any exceptions

## Common Failures

- One volunteer who knows every password, then leaves
- A donated computer put into use with its old system and the last owner's files still on it
- Updates turned off "until later"
- Backups that were never tested, or kept only on site
- Residents' private devices on the same network as the office computer and the camera recorder
- Members' records saved on a public computer
- The router still using its default password
- Asking residents to change what runs on their own devices. The rule covers community systems only.
- Copper network cable run between buildings, then destroyed by a lightning strike
- Burying fiber without conduit, or digging a trench without laying spare conduit
- No spare strands, so one damaged strand means a new cable
- No map of the fiber runs, so a digger cuts one

## Money Tie-In

- Track hardware, storage, internet, and backup costs in the [expense log](../appendices/appendix-d-logs-sheets-and-reports/d06-expense-log.md)
- Accept donated hardware, but wipe it and install a fresh system before use
- Pay a local technician for setup if no member has the skills, and have them train the two administrators
- Most of the cost of fiber is digging and conduit, not the cable. Lay conduit during trench and road work, and pull fiber later as funds allow ([capital plan](../appendices/appendix-d-logs-sheets-and-reports/d20-capital-plan-and-build-order.md))

> Data protection, privacy, children's online safety, and record-keeping rules differ by location. This handbook gives no legal advice, so check what applies to the records and computers you keep, and ask an attorney before collecting members' personal data.

<!-- nav: generated by scripts/nav.py, do not edit below -->

---

← **Previous:** [Bonus](README.md)
