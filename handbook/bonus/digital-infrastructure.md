[Handbook](../../README.md) › [Bonus](README.md) ›

# Digital Infrastructure: Linux and BSD

## Rule

**If the community uses digital infrastructure or public computers, they run Linux or one of the BSDs.** That covers every computer, server, and network device the community owns, runs, or offers for shared use. **Private devices are not subject to this rule.** A resident's own phone, laptop, tablet, or game console can run anything its owner likes.

This page is a bonus. It sits outside the tier triggers. Add it to the charter by a vote when the community first sets up a shared computer, a network, or a server, and add it to your [revision log](../../REVISION_LOG.md).

## What It Covers

| Covered (Linux or BSD) | Not covered |
|---|---|
| Community servers: file storage, backups, the shared calendar, the website | Residents' own phones, laptops, tablets, and desktops |
| The router, firewall, and Wi-Fi access points the community runs | Visitors' devices |
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

## When a Required Program Won't Run

Sometimes a bank, a tax office, or an accountant uses software made only for Windows or macOS. Work through these steps in order:

1. **Use the web version.** Most banking, tax filing, and payment services work in a browser on Linux or BSD.
2. **Use the professional's own systems.** Send the accountant or attorney the files, and let them run their software.
3. **Ask for another format,** such as a spreadsheet or PDF instead of a program file.
4. **Only if all three fail,** the board may approve a narrow written exception for that one task. Record the reason and the date in the revision log, keep the machine off the community network, store no community records on it, and review the exception every year.

## Tier Fit

- **Tier 0:** no community computers are needed. Private phones and laptops are fine. If the group takes in a shared or donated computer, it runs Linux or BSD from the start.
- **Tier 1:** one office computer for the logs, budget, and filings, with two administrators and an off-site backup
- **Tier 2:** a community router and firewall with a guest network, and a camera recorder on its own network with off-site storage
- **Tier 3:** a small server for files, the shared calendar, and backups, the Meeting Hall recorder and archive storage, and a public computer in the Lodge
- **Tier 4:** a yearly review of systems, updates, backups, accounts, and any exceptions

## Common Failures

- One volunteer who knows every password, then leaves
- A donated computer put into use with its old system and the last owner's files still on it
- Updates turned off "until later"
- Backups that were never tested, or kept only on site
- Residents' private devices on the same network as the office computer and the camera recorder
- Members' records saved on a public computer
- The router still using its default password
- Asking residents to change what runs on their own devices. The rule covers community systems only.

## Money Tie-In

- Track hardware, storage, internet, and backup costs in the [expense log](../appendices/appendix-d-logs-sheets-and-reports/d06-expense-log.md)
- Accept donated hardware, but wipe it and install a fresh system before use
- Pay a local technician for setup if no member has the skills, and have them train the two administrators

> Data protection, privacy, children's online safety, and record-keeping rules differ by location. This handbook gives no legal advice, so check what applies to the records and computers you keep, and ask an attorney before collecting members' personal data.

<!-- nav: generated by scripts/nav.py, do not edit below -->

---

← **Previous:** [Bonus](README.md)
