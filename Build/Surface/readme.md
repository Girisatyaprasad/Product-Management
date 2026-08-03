# Surface

# Executive Summary

Face-to-face prospecting professionals rely on multiple disconnected applications to present proof, capture prospect information, and retrieve previous interactions. This fragmented workflow interrupts conversations, increases cognitive load, and leads to context loss over time.

Surface is a privacy-first mobile application that unifies prospect information management into a single workflow, enabling professionals to capture, organize, and retrieve prospect context without disrupting live interactions.

# Product Overview

## Surface

Surface is a mobile application designed for face-to-face prospecting professionals. It enables users to capture, organize, and retrieve prospect information through a unified workflow, reducing app switching and preserving relationship context for future interactions.

# Target Users

### Primary Users

- Network Marketers
- Solo Entrepreneurs

### Secondary Users

- Real Estate Agents
- Sales Representatives

### Non-target Users

- General consumers
- Large enterprise sales teams

# Problem Statement

Face-to-face prospecting professionals depend on multiple disconnected applications to present proof, capture prospect information, and document interactions. Constant app switching interrupts conversations, increases cognitive effort, and fragments prospect information across different tools.

As prospect volume grows, professionals struggle to retrieve previous conversations, identify prospects accurately, and maintain meaningful relationship context, resulting in inefficient follow-ups and missed opportunities.

# Vision

To become the default operating system for face-to-face prospecting by making prospect information effortless to capture, organize, and retrieve while preserving user privacy and minimizing workflow complexity.

# Core Value Proposition

Surface enables face-to-face prospecting professionals to capture, organize, and retrieve prospect context within a single privacy-first workflow, reducing app switching, preserving relationship history, and improving the quality of every prospect interaction.

# Users

### Primary Users

- Network Marketers
- Solo Entrepreneurs

### Secondary Users

- Real Estate Agents
- Sales Representatives

### Non-target Users

- General consumers
- Large organizations requiring CRM platforms

# Jobs To Be Done

## Functional Job

Help professionals capture, organize, and retrieve prospect information quickly without interrupting face-to-face conversations.

## Emotional Job

Give professionals confidence that every prospect interaction is documented, organized, and easily retrievable, reducing the anxiety of forgetting important details.

## Social Job

Help professionals appear organized, attentive, and well-prepared by enabling them to recall prospect information and previous interactions naturally during conversations.

## Core Job

Enable face-to-face prospecting professionals to preserve relationship context and retrieve prospect information effortlessly while maintaining a smooth and uninterrupted prospecting workflow.

## Product Principles

- Local-First privacy.
- Focuses more on Retrieval over storage
- User control over all operations
- Preserve context, not just information
- Minimize cognitive load

## Metrics

### North Star Metrics

- Successful Context Retrievals

### Primary Success Metrics

- Retrieval Success Rate
- Average Retrieval Time

### Secondary Success Metrics

- Context Completeness Score
- Search Success Rate
- Average Blocks per Prospect
- Photos/Notes/Contacts linked
- Profile Completion Rate

# User Journey

### Journey 1 — New Prospect

### Goal

Capture a new prospect without interrupting the conversation.

### Steps

1. Meet a new prospect.
2. Build rapport and understand their needs.
3. Present relevant proof (images, testimonials, presentations).
4. Create a new prospect.
5. Capture contact information.
6. Take a profile photo (optional).
7. Add quick notes.
8. Assign categories.
9. Save.

### Success Criteria

- Prospect is created in under one minute.
- Conversation remains uninterrupted.
- All information stays connected to the prospect.

---

### Journey 2 — Follow-up

### Goal

Recall previous interactions before meeting again.

### Steps

1. Open Surface.
2. Search for the prospect.
3. View previous notes.
4. Review photos.
5. Recall products discussed.
6. Continue the conversation naturally.

### Success Criteria

- Prospect found within a few seconds.
- Context retrieved without searching multiple apps.

---

### Journey 3 — Information Retrieval

### Goal

Retrieve information during a live conversation.

### Steps

1. Prospect asks a question.
2. Open Surface.
3. Open the prospect.
4. Find the required proof.
5. Show it.
6. Continue the conversation.

### Success Criteria

- Minimal interruption.
- Proof found quickly.
- Conversation flow maintained.

---

### Journey 4 — Updating Context

### Goal

Keep prospect information up to date.

### Steps

1. Open existing prospect.
2. Add new notes.
3. Add new photos.
4. Update categories.
5. Save.

### Success Criteria

- New information is immediately connected to the existing prospect.

---

### Journey 5 — Preparing Before Prospecting

### Goal

Prepare everything before going out.

### Steps

1. Organize proof.
2. Review today's prospects.
3. Check follow-ups.
4. Leave for prospecting.

### Success Criteria

- Required material is ready before meeting prospects.

# Information Architecture

## Overview

Surface organizes information around a single core object called a **PIN (Prospect Information)**.

Each PIN represents one prospect and contains all information collected throughout the relationship. Instead of storing contacts, notes, photos, and proof across multiple applications, Surface keeps everything connected inside a single PIN to preserve context and enable fast information retrieval.

# Core Information Unit

## PIN (Prospect Information)

A PIN is the fundamental information unit within Surface.

Each PIN represents a single prospect and serves as the central place where all information related to that prospect is stored and managed.

A PIN may contain:

- Contact Information
- Profile Photo
- Notes
- Categories
- Proof Assets
- Interaction History

Every PIN is created and managed manually by the user to ensure complete accuracy, privacy, and user control.

# Information Hierarchy

```
Surface
│
├── Home
│   ├── PIN
│   │   ├── Contact Information
│   │   ├── Profile Photo
│   │   ├── Notes
│   │   ├── Categories
│   │   ├── Proof Assets
│   │   └── Interaction History
│   │
│   └── PIN
│       └── ...
│
└── Settings
```

# Information Relationships

Every piece of information belongs to a single PIN.

```
PIN
│
├── Contact Information
├── Profile Photo
├── Notes
├── Categories
├── Proof Assets
└── Interaction History
```

Surface does not automatically infer relationships between information. Users explicitly associate information with the appropriate PIN, ensuring reliable organization and preserving user privacy.

# Categories

Categories classify prospects based on business context.

Examples include:

- Weight Loss
- Diabetes
- Skin Care
- Business Opportunity
- Insurance
- Investment

A single PIN can belong to multiple categories.

# Proof Assets

Proof Assets are supporting materials used during prospecting.

Examples include:

- Before & After Images
- Testimonials
- Product Images
- Presentations
- Documents
- Videos

Proof Assets are linked to the relevant PIN to maintain context during future interactions.

# Interaction History

Interaction History records meaningful events throughout the relationship with a prospect.

Examples include:

- PIN Created
- Note Added
- Profile Photo Added
- Proof Shared
- Category Assigned
- Follow-up Completed

Interaction History provides a chronological record that helps professionals understand previous interactions before reconnecting with a prospect.

# Design Principles

Surface's information architecture is guided by the following principles:

- **PIN-first organization** — Every interaction begins with a PIN.
- **Context over isolated data** — Preserve the relationship, not just individual pieces of information.
- **Explicit user control** — Information is associated manually to ensure accuracy.
- **Privacy-first** — Surface never analyzes user content to infer relationships.
- **Local-first** — User data remains under the user's control.
- **Fast retrieval** — Information should be accessible within seconds.
- **Low cognitive load** — Information should be organized naturally without overwhelming the user.

# Core Features

- **PIN** — Central record for a prospect.
- **Gallery** — Store and present proof assets.
- **Notes** — Store textual information.
- **Camera** — Capture profile and proof photos.
- **Categories** — Organize prospects by business context.
- **History** — Chronological record of interactions.
- **Search** — Find PINs and retrieve information quickly.

## PIN

### Overview

PIN is the core information unit of Surface. Every PIN represents a single prospect and serves as the central place where all information related to that prospect is stored.

### Purpose

Preserve prospect context in a single location.

### User Problem

Prospect information is scattered across multiple applications, making retrieval difficult and causing context loss.

### Solution

Keep all prospect-related information connected inside one PIN.

### User Flow

Create PIN → Add Information → Update Information → Retrieve Information

### Success Criteria

- PIN creation completed within 30 seconds.
- Users update existing PINs instead of creating duplicates.
- Prospect context retrieved within a few seconds.

---

## Gallery

### Overview

Gallery stores all visual proof used during prospecting, including testimonials, transformations, product images, presentations, and other supporting media.

### Purpose

Present visual proof quickly without switching applications.

### User Problem

Visual proof is scattered across the phone gallery, making retrieval slow and interrupting conversations.

### Solution

Keep all business-related visual assets accessible within Surface.

### User Flow

Open Gallery → Select Proof → Present → Return to Conversation

### Success Criteria

- Required proof located within 5 seconds.
- Reduced switching to the system gallery.
- Faster proof presentation during meetings.

---

## Notes

### Overview

Notes stores textual information related to a prospect, including personal details, interests, objections, reminders, and conversation summaries.

### Purpose

Preserve valuable information that cannot be captured visually.

### User Problem

Important details are forgotten after conversations or scattered across different note-taking apps.

### Solution

Allow professionals to record and retrieve notes directly from the corresponding PIN.

### User Flow

Open PIN → Add Note → Save → Retrieve During Follow-up

### Success Criteria

- Notes created in under 20 seconds.
- Notes remain linked to the correct PIN.
- Information easily retrievable during follow-ups.

---

## Camera

### Overview

Camera allows professionals to capture profile photos and business-related images directly within Surface.

### Purpose

Capture visual information without leaving the workflow.

### User Problem

Using the system camera interrupts conversations and requires manual organization afterward.

### Solution

Capture photos directly inside Surface and immediately associate them with the current PIN.

### User Flow

Open Camera → Capture Photo → Save to PIN

### Success Criteria

- Photo captured in under 10 seconds.
- Photo automatically stored inside the current PIN.
- No manual importing required.

---

## Categories

### Overview

Categories organize prospects based on business context, interests, or requirements.

### Purpose

Improve organization and retrieval.

### User Problem

As the number of prospects grows, locating specific groups becomes increasingly difficult.

### Solution

Allow users to assign one or more categories to each PIN.

### User Flow

Open PIN → Select Categories → Save → Filter/Search

### Success Criteria

- Categories assigned within a few taps.
- Category filtering reduces search effort.
- Users consistently organize new PINs.

---

## History

### Overview

History records significant interactions performed within each PIN in chronological order.

### Purpose

Help professionals understand previous interactions before reconnecting with a prospect.

### User Problem

Users forget when and how previous interactions occurred.

### Solution

Maintain a timeline of activities for every PIN.

### User Flow

Open PIN → View History → Review Previous Activities

### Success Criteria

- Complete interaction timeline available.
- Important events never lost.
- Faster preparation before follow-ups.

---

## Search

### Overview

Search enables professionals to quickly locate prospects and retrieve related information.

### Purpose

Reduce retrieval time during prospecting and follow-ups.

### User Problem

Finding the correct prospect becomes difficult as the number of PINs increases.

### Solution

Provide fast search across PINs using available information.

### User Flow

Search → Select PIN → Retrieve Information

### Success Criteria

- Search results displayed instantly.
- Desired PIN found within seconds.
- Reduced retrieval effort.

---

## Contact Information

### Overview

Contact Information stores the primary identity and communication details of a prospect.

### Purpose

Maintain accurate prospect identity.

### User Problem

Prospect identities are difficult to recall when information is incomplete or scattered.

### Solution

Store contact details as part of every PIN.

### User Flow

Create PIN → Add Contact Information → Save → Update When Needed

### Success Criteria

- Contact details captured accurately.
- Easy updates.
- Information remains linked to the correct PIN.

## Functional Requirements

This is where you define **what the system must do**.

Think of it as a contract between Product and Engineering.

Example:

## PIN

### The system shall:

- Create a new PIN.
- Edit an existing PIN.
- Delete a PIN.
- Archive a PIN.
- Restore an archived PIN.
- Search PINs.
- Associate notes with a PIN.
- Associate gallery items with a PIN.
- Associate categories with a PIN.
- Display interaction history.
- Display profile information.

---

## Gallery

### The system shall:

- Capture photos.
- Import photos from the device.
- Display gallery items.
- Delete gallery items.
- Associate gallery items with a PIN.
- Preview images.
- Support full-screen viewing.

---

## Notes

### The system shall:

- Create notes.
- Edit notes.
- Delete notes.
- Attach notes to a PIN.
- Display notes chronologically.
- Support multiline text.

---

## Camera

### The system shall:

- Capture profile photos.
- Capture proof images.
- Associate captured images with the active PIN.
- Retake photos.
- Save captured photos.

---

## Categories

### The system shall:

- Create categories.
- Rename categories.
- Delete categories.
- Assign multiple categories to a PIN.
- Remove categories from a PIN.
- Filter PINs by category.

---

## History

### The system shall:

- Record major actions.
- Display activities chronologically.
- Associate activities with a PIN.
- Allow users to review previous interactions.

---

## Search

### The system shall:

- Search by name.
- Search by phone number.
- Search by notes.
- Search by category.
- Display matching PINs instantly.
- Open a selected PIN.

## Non-functional Requirements

## Performance

Surface shall provide a fast and responsive experience during live prospecting.

### Requirements

- App launch time should be less than **2 seconds**.
- PIN creation should complete within **30 seconds**.
- Search results should appear within **500 milliseconds**.
- PINs should open within **300 milliseconds**.
- Gallery items should load within **1 second**.
- Camera should launch within **1 second**.
- UI interactions should remain smooth at **60 FPS**.

---

## Privacy

Surface shall prioritize user privacy and data ownership.

### Requirements

- User content shall never be analyzed to infer relationships.
- Surface shall not use user data for advertising.
- User data shall remain under the user's control.
- Permission requests shall only occur when required.
- Users shall be informed before accessing sensitive device permissions.

---

## Security

Surface shall protect user information from unauthorized access.

### Requirements

- User data shall be encrypted at rest.
- Sensitive information shall be protected using platform security features.
- Authentication shall be required before accessing protected data (when enabled).
- Deleted data shall not remain accessible through the application.

---

## Reliability

Surface shall provide a dependable experience.

### Requirements

- User data shall persist after application restarts.
- Data shall not be lost during unexpected crashes.
- Save operations shall complete reliably.
- The application shall recover gracefully after interruptions.

---

## Offline Capability

Surface shall function without internet connectivity.

### Requirements

- Users shall be able to create PINs offline.
- Users shall be able to edit PINs offline.
- Gallery shall remain accessible offline.
- Notes shall remain accessible offline.
- Search shall function offline.
- Core prospecting workflows shall not depend on an internet connection.

---

## Usability

Surface shall minimize cognitive load during face-to-face prospecting.

### Requirements

- Frequently used actions shall require minimal interaction.
- Navigation shall remain simple and consistent.
- Users shall complete common tasks without training.
- Prospect information shall remain easy to locate.
- Interface elements shall be readable under outdoor lighting conditions.

---

## Accessibility

Surface shall be usable by a broad range of users.

### Requirements

- Text shall remain legible at different system font sizes.
- Interactive elements shall provide adequate touch targets.
- Icons shall be supported by descriptive labels.
- Color shall not be the only method of conveying information.

---

## Scalability

Surface shall continue to perform efficiently as user data grows.

### Requirements

- Performance shall remain consistent with thousands of PINs.
- Search performance shall remain fast regardless of data size.
- Gallery performance shall remain responsive as media grows.
- Application startup time shall not degrade significantly over time.

---

## Compatibility

Surface shall support the intended Android ecosystem.

### Requirements

- Support current and recent Android versions.
- Support multiple screen sizes and resolutions.
- Support portrait orientation.
- Integrate with native camera and contacts where appropriate.

---

## Maintainability

Surface shall be designed for long-term development and evolution.

### Requirements

- Features shall be modular and independently maintainable.
- Code shall follow consistent architecture and standards.
- New features shall minimize impact on existing functionality.

---

## Design Consistency

Surface shall provide a predictable and coherent user experience.

### Requirements

- Navigation patterns shall remain consistent throughout the application.
- Visual components shall follow a unified design system.
- Animations shall support usability rather than decoration.
- Feedback shall be provided for important user actions.

---

## Future Readiness

Surface shall support future enhancements without compromising current functionality.

### Requirements

- The architecture shall accommodate future capabilities such as AI-assisted workflows.
- Future features shall preserve Surface's privacy-first principles.
- New functionality shall not introduce unnecessary complexity into core prospecting workflows.

### Scope

Define exactly what you're building.

**In Scope (V1)**

- PIN
- Gallery
- Notes
- Camera
- Categories
- History
- Search

**Out of Scope**

- AI auto-linking
- Cloud collaboration
- Team workspaces
- CRM integrations
- Voice notes
- OCR
- AI-generated summaries

---

### Assumptions

These are beliefs you're making before validating.

Examples:

- Users primarily prospect face-to-face.
- Users are comfortable manually creating PINs.
- Users value privacy over automation.
- Fast retrieval is more important than automatic organization.

---

### Constraints

These are decisions or limitations.

Examples:

- Android-first.
- Offline-first.
- Local-first storage.
- No analysis of user content.
- No cloud dependency for core workflows.

---

### Risks

What could go wrong?

Examples:

- Users forget to create a PIN after a meeting.
- Duplicate PINs increase over time.
- Gallery becomes cluttered.
- Manual organization feels time-consuming.
- Search quality declines with large datasets.

---

### Open Questions

Questions that still need answers.

For example:

- Should categories be user-defined or predefined?
- Should Gallery support PDFs in V1?
- Should History be editable?
- Should deleted PINs go to Trash?
- Should Search be global or PIN-specific?

---

### Release Plan

Break the roadmap into versions.

**V1 (MVP)**

- PIN
- Gallery
- Notes
- Camera
- Categories
- Search
- History

**V1.1**

- Backup & Restore
- Import Contacts
- Better Search

**Future**

- Surface Algorithm
- Team support
- Cloud Storage
- Copilot

## Market Sizing

|  | Market | Users | Basis |
| --- | --- | --- | --- |
| **TAM** | Global direct-selling market | **104.3M** | WFDSA global independent representatives |
| **SAM** | Indian direct-selling market | **9.32M before workflow filtering** | IDSA direct sellers |
| **Initial SOM** | Reachable distributor network | **TBD from actual distribution funnel** | Bottom-up: reachable distributors → adoption → paid conversion |

## RICE

| Feature | Reach | Impact | Confidence | Effort | Score |
| --- | --- | --- | --- | --- | --- |
| Notes | 5 | 5 | 3 | 1 | **75.0** |
| Gallery | 5 | 5 | 3 | 2 | **37.5** |
| PIN | 5 | 5 | 3 | 4 | **18.8** |
| Camera | 4 | 4 | 2 | 3 | **10.7** |
| Search | 3 | 3 | 2 | 2 | **9.0** |
| History | 2 | 3 | 2 | 2 | **6.0** |

## User Flow Artifact

#### Core product loop

MEET
Face-to-face interaction
↓
PRESENT
Open Surface Gallery
→ Find relevant category
→ Show proof/assets
↓
CAPTURE
New PIN
→ Name
→ Phone
→ Problem/context
→ Optional photo
→ Save
↓
BIND
Photos + notes + contact information
stay associated with that prospect
↓
RETRIEVE
Days/weeks later
→ Search by name / phone / problem / context
OR visually browse PINs
↓
RECALL
Surface restores:
Who they are
What they needed
What happened previously
Relevant visual context
↓
FOLLOW UP
Representative continues the relationship
with context instead of relying on memory
↓
UPDATE
New information is added to the PIN
↓
REPEAT

#### Flow 1 — Live Prospecting

Meet Prospect
→ Surface
→ Gallery
→ Category
→ Show Relevant Assets
→ New PIN
→ Capture Name + Phone + Context
→ Optional Photo
→ Save
→ PIN Created

#### Flow 2 — Capture During/After Interaction

Important context appears
↓
Camera / Notes
↓
Capture information
↓
Existing prospect?
↙         ↘
YES          NO
↓            ↓
Bind to PIN    Create PIN
↘          ↙
Context preserved

**Camera**

Capture Photo
→ Preview
→ + New PIN
OR
→ ✓ Save
OR
→ ↻ Retake

#### Flow 3 — Follow-Up

Need to follow up
→ Surface Search
→ Search name / phone / problem / context
→ Best Match
→ Open PIN
→ Recall person + previous context
→ Follow up
→ Add new information
→ PIN becomes richer

## Market Sizing

| Layer | Market | Users |
| --- | --- | --- |
| **TAM** | Global direct sellers | ~104.3M |
| **SAM** | Indian direct sellers | ~9.32M* |
| **SOM** | Initial realistically obtainable users | **500** |
| **Year-1 Goal** | 0.5% of Indian market | ~46,600 |

# Surface V1 — Interaction Design Specification

## 1. Navigation & Motion

Surface motion must feel fast, controlled, and functional. Animations should communicate navigation or state changes rather than exist as decoration.

| Interaction | Motion |
| --- | --- |
| Home → Gallery | Slide left |
| Home → Notes | Slide left |
| Home → PINs | Slide left |
| Gallery / Notes / PINs → Home | Slide right |
| Home → Camera | Camera tile expands into full-screen camera |
| Camera → Home | Camera view collapses toward its Home tile |
| PIN → All PINs | Short crossfade + subtle scale |
| Search | Minimal fade/state transition |
| Menu | Short slide/fade overlay |

The **Camera transition is Surface's primary high-fidelity animation**. Other navigation should remain lightweight to preserve performance.

If the device cannot maintain smooth animation, Surface should automatically favor a simpler transition rather than allowing dropped frames.

---

## 2. Motion Timing & Character

Surface should not feel playful, elastic, or excessively animated.

Motion character:

> **Fast initiation → smooth deceleration → stable finish**
> 

Approximate timing targets:

| Motion | Duration |
| --- | --- |
| Micro-interaction | 100–160 ms |
| Button/state transition | 150–200 ms |
| Normal page navigation | 200–260 ms |
| Camera expansion/collapse | 280–350 ms |

Avoid:

- Excessive spring animations
- Long transitions
- Continuous decorative animation
- Large parallax effects
- Animation that delays user input

Respect the operating system's reduced-motion/accessibility preferences.

---

## 3. Haptic System

Haptics communicate **meaningful state changes**, not ordinary taps.

### Selection haptic

Very subtle.

Used for:

- Gallery category selection
- PIN selection where appropriate
- Image selection
- PIN photo settling after swipe

### Confirmation haptic

Short, clean confirmation.

Used for:

- PIN created
- Note saved
- Photo saved
- Asset successfully bound

### Camera capture haptic

One crisp tactile pulse synchronized with successful image capture.

**Surface does not intentionally play a shutter sound.**

Where the operating system/device legally or technically requires camera capture sounds, Surface must respect the system behavior rather than attempting to bypass it.

### Long-press haptic

One subtle pulse when the long-press action threshold is reached.

### Error/destructive haptic

Distinct from confirmation feedback and reserved for genuine warnings, failures, or destructive actions.

### No haptic

Do not generate haptics for:

- Normal navigation
- Scrolling
- Opening menus
- Typing
- Every button press
- Continuous swipe movement

---

## 4. Camera Interaction

Surface Camera is a **fast capture utility**, not a full photography application.

No:

- Filters
- Beauty modes
- Editing tools
- Photography modes
- Unnecessary camera controls

### Capture flow

```
Open Camera
↓
Live Preview
↓
Capture
↓
Crisp Haptic + Silent Capture
↓
Freeze Captured Image
↓
Post-Capture View
```

The user **cannot immediately take another photograph after capture**.

The captured image must first be accepted or rejected.

### Post-Capture actions

**Retake**

Discard current capture → immediately restore camera preview.

**+ New PIN**

Keep captured image → open New PIN → image automatically becomes associated with the new PIN.

**✓ Save**

Save image to Surface → provide subtle confirmation → return to the appropriate Surface state.

The interaction should resemble the simplicity of an Instagram-style capture-confirm-retake workflow without Surface implementing filters or social-camera functionality.

---

## 5. Gallery & PIN Asset Treatment

Images are primary information objects in Surface.

### Asset border

All Gallery/PIN image assets use:

**2 px solid black border**

The border is part of Surface's visual identity and should remain consistent across supported asset presentations.

### Text over imagery

When text must appear over an image:

- Apply **localized high-quality background blur only underneath/around the text region**.
- The rest of the image remains sharp.
- Blur exists strictly to preserve readability.
- Blur should feel integrated with the image rather than appearing as a generic translucent glass panel.

Avoid cheap-looking full-card blur or excessive glassmorphism.

### Corners

Image containers should follow Surface's established rounded geometry consistently. Avoid arbitrary corner-radius variations between screens.

---

## 6. Touch & Gesture Behaviour

Every interactive element must provide immediate visual acknowledgement on touch.

### Tap

Visual feedback begins on **finger-down**, not after navigation starts.

### Long press

Reserved for secondary actions where it reduces permanent UI clutter.

Example:

```
Long press Note
↓
Group
Edit
Delete
```

A subtle haptic fires when the long-press threshold is reached.

### PIN photo swipe

One PIN may contain multiple contextual photographs, such as:

- Prospect
- Family
- House
- Location
- Other relevant context

Horizontal swipe navigates photographs belonging to the **same PIN**.

No repeated haptic while dragging.

A subtle selection haptic occurs when the next image settles into position.

Gestures must never interfere with normal scrolling or system navigation.

---

## 7. Loading & Perceived Performance

Surface should avoid visible loading whenever useful local information can already be displayed.

### Principle

> **Show useful information immediately; resolve heavier assets afterward.**
> 

### Local content

Render immediately whenever available.

### Gallery

Load lightweight/cached thumbnails first.

Load higher-resolution assets only when required.

### PINs

Render:

1. Text/context
2. Available thumbnail
3. Higher-resolution imagery as needed

Do not block an entire PIN because one image is still loading.

### Camera

Camera-preview startup takes priority over secondary interface elements.

Surface generates no application-level shutter sound. System/OEM-enforced camera sounds remain outside Surface's control.

### Loading indicators

Do not show a spinner for operations that complete quickly enough that the indicator itself creates more perceived latency.

When loading is genuinely required, prefer stable placeholders over disruptive full-screen loaders.

---

## 8. Performance Requirements

Surface must remain responsive on **4 GB RAM Android devices**.

Premium appearance must never come at the expense of responsiveness.

### Prioritize

- Opacity
- Translation
- Simple scale
- Efficient GPU-accelerated transformations
- Thumbnail caching
- Lazy image loading
- Memory-efficient image decoding

### Minimize

- Multiple simultaneous complex animations
- Full-resolution images loaded unnecessarily
- Persistent background animations
- Large shadow effects
- Repeated real-time blur computation
- Unnecessary compositing layers
- Heavy transitions between ordinary screens

Localized blur used on PIN/Gallery text regions must be implemented efficiently and tested specifically on lower-memory devices.

### Performance rule

> **If visual fidelity and responsiveness conflict, responsiveness wins.**
> 

A simple transition running smoothly is superior to a sophisticated transition dropping frames.

---

## 9. Error & State Feedback

Surface should communicate failures without interrupting the user's workflow unnecessarily.

### Successful action

Use:

- Immediate visual state change
- Subtle confirmation haptic
- Small temporary confirmation message when useful

Example:

> **New PIN created ✓**
> 

Avoid dedicated success screens for routine actions.

### Recoverable error

Keep the user on the current screen and preserve entered information.

Example:

> **Couldn't save. Try again.**
> 

Never erase user-entered PIN information because a save/network operation failed.

### Offline behaviour

Core local workflows should continue functioning wherever technically possible.

Network failure should not prevent:

- Opening existing local PINs
- Viewing locally available Gallery assets
- Writing local Notes
- Creating locally stored PINs
- Using Camera

Synchronization can resume when connectivity returns.

---

## 10. Surface Interaction Principle

Every interaction should pass three tests:

> **Does it make the action clearer?**
> 
> 
> **Does it make Surface feel faster?**
> 
> **Does it preserve performance on low-end hardware?**
> 

If an animation, haptic, blur, gesture, or visual effect fails all three, **remove it**.

Surface should feel premium because it is **responsive, predictable and precise**, not because it contains more effects.

## 1. Surface Pro — Entitlement & Upgrade System

### Surface Basic

Basic should preserve the user's existing information and fundamental access.

**Available:**

- View existing PINs
- View existing photos
- View existing notes
- Browse Gallery
- Camera
- Copy phone numbers/text/details
- Exact-match search
- Local access to existing information

**Pro-gated:**

- Create new PINs
- Edit existing PIN information
- Bind new notes/photos/context to PINs
- Smart/fuzzy/contextual search
- Home-screen widgets
- Future Pro capabilities
- Cloud backup when introduced

### Search distinction

Basic:

```
Stored:
Giri Satya

Search:
Giri Satya     → Found
Giri           → No result
Satya          → No result
Giri S         → No result
```

Pro:

```
Giri
Giri Satya
Satya
phone number
problem
location
other indexed context
        ↓
Relevant PIN
```

That's a **real feature difference**:

> Basic = deterministic exact retrieval.
> 
> 
> Pro = intelligent contextual retrieval.
> 

---

## Surface Pro high-fidelity screen

Yes, this deserves an actual Canva screen because it's directly responsible for revenue.

I wouldn't make it look like a generic SaaS pricing table.

Something closer to:

```
SURFACE PRO

        Surface
          PRO

Remember more.
Find anything.
Keep moving.

✓ Create & continuously update PINs
✓ Smart Search
✓ Bind context
✓ Surface Widgets
✓ Pro features as they arrive

          ₹149
         / month

1 MONTH     3 MONTHS     6 MONTHS

       GET SURFACE PRO

Cancel anytime
```

For Beta launch, replace ₹149 with your ₹99 Beta Pro price if that's still the launch decision.

Use the Surface visual language heavily here. **This screen sells the product.**

---

## 2. Paywalls, Errors & Upgrade Prompts

Don't create separate full-screen paywalls for every blocked action.

Use one consistent **Pro Gate component**.

### Example — New PIN

Basic user taps `+`.

Modal:

> **Create more with Surface Pro**
> 
> 
> Creating new PINs is available with Surface Pro.
> 
> `×` **Get Surface Pro**
> 

Cross left. CTA right.

### Example — Edit

> **Keep your PINs updated**
> 
> 
> Editing PIN information requires Surface Pro.
> 
> `×` **Get Surface Pro**
> 

### Example — Bind

> **Add more context with Pro**
> 
> 
> Adding new information to existing PINs requires Surface Pro.
> 
> `×` **Get Surface Pro**
> 

### Basic Search — No Exact Match

This one needs special treatment.

First:

> **Oops, I didn't find that.**
> 
> 
> Try the exact name or information stored in your PIN.
> 

If they attempt to create from there:

> **Create new PINs with Surface Pro**
> 
> 
> Upgrade to continue.
> 
> `×` **Get Surface Pro**
> 

But I **would not immediately blame Basic every time search fails**. A Pro user can search for something that genuinely doesn't exist too.

For Basic, you could subtly add:

> **Surface Pro can search partial names and context.**
> 

That's a much cleaner upsell.

### Payment failure

> **We couldn't renew Surface Pro.**
> 
> 
> Your existing information is safe. Update your payment method to continue using Pro features.
> 
> **Manage Payment**
> 

### Expired

> **Surface Pro has ended.**
> 
> 
> Everything you've already saved remains available. Creating and updating information now requires Pro.
> 
> **Renew Surface Pro**
> 

That's important: **never make users fear that Surface deleted their information.**

---

## 3. Help, Feedback & Privacy

These can share infrastructure, but they're separate user experiences.

## Help & Feedback

Keep it tiny:

```
HELP & FEEDBACK

Getting Started
Using PINs
Gallery & Camera
Surface Pro

Report a Problem
Suggest an Improvement
Contact Surface
```

### Report a Problem

Ask:

> **What happened?**
> 

Allow screenshot attachment.

With consent, attach technical diagnostics such as:

- Surface version
- Android version
- Device model
- Error identifier

### Feedback

Don't ask:

> What feature should we build?
> 

Ask:

> **What were you trying to do?**
> 
> 
> **What made it difficult?**
> 

That's directly aligned with the continuous product-learning system you want.

---

## Privacy & Security

In-app:

```
PRIVACY & SECURITY

App Lock
Permissions
Data Collection
Privacy Policy
Delete My Data
```

And your actual Privacy Policy lives on the Surface website as well.

Most importantly, your telemetry architecture should use **events rather than blindly uploading user content**.

For example:

```
pin_created
pin_opened
search_performed
search_success
search_failed
gallery_opened
asset_viewed
camera_capture
pro_gate_seen
pro_gate_converted
```

You generally need the **event**, not the person's private note or photograph.

---

# 4. Subscription Lifecycle

This is the part we define before backend work.

```
NEW USER
    ↓
SURFACE BASIC
    ↓
Sees Pro value / hits Pro gate
    ↓
SURFACE PRO PAGE
    ↓
Chooses duration
1 / 3 / 6 months
    ↓
Store purchase
    ↓
Purchase verified
    ↓
SURFACE PRO ACTIVE
    ↓
       ┌──────────── Renewal successful
       │                    ↓
       │               PRO CONTINUES
       │
Renewal date
       │
       └──────────── Payment fails
                            ↓
                     Retry / Grace
                            ↓
                   ┌────────┴────────┐
                 Paid             Unpaid
                   ↓                  ↓
                  Pro           BASIC MODE
                                      ↓
                              Existing data remains
                                      ↓
                              User resubscribes
                                      ↓
                                   PRO
```

### Entitlement rule

Backend/app shouldn't think:

> `"user_paid = true"`
> 

Think:

```
entitlement = PRO
valid_until = timestamp
```

Then every gated capability asks:

> **Does this account currently have the required entitlement?**
> 

Not:

> Did they once pay?
> 

That architecture will save you trouble later.

## Plan

| Version | Product stage | Major change |
| --- | --- | --- |
| **X1** | Baby | Core Surface |
| **X2** | Kindergarten | Gallery + Notes become more capable |
| **X3** | 1st standard | Search |
| **X4** | 2nd standard | Widgets |
| **X5** | 3rd standard | Better/more configurable widgets |
| **X6** | 4th standard | Better Follow-up |
| **X7** | 5th standard | IIS-driven productivity upgrade |
| **X8–X9** | Growing | Determined from accumulated evidence |
| **Y** | Next era | Surface has enough behavioral evidence to evolve more intelligently |

### X1 — Core Surface

Ship only what establishes the product:

- Home
- Gallery — basic flat view, **no categories**
- Notes — basic writing, **no copy**
- Camera
- PINs
- Direct `+ New PIN`
- Basic PIN editing
- Copy PIN information
- Call action
- WhatsApp action
- Basic follow-up scheduling
- One fixed Surface follow-up initiation framework
- Surface Pro/subscription infrastructure
- IIS telemetry foundation

No Search.

No widgets.

No Gallery categories.

No advanced Notes.

No lock.

No productivity system.

### X2 — **Your notes, with more power.**

This becomes the first visible proof that Surface evolves.

**Notes**

- Copy note/content
- Markdown foundation remains
- Better editing capabilities as justified
- Existing X1 notes remain completely intact

Importantly, you're **not having AI restructure notes** into headings/lists automatically. The Markdown-compatible structure exists underneath; X2 exposes more useful capabilities to the user.

**Gallery**

- Categories arrive
- Basic category organization
- Normal category view
- Improved asset management

Again, don't overbuild categories. X2 introduces the organizational primitive.

Surface announcement:

> **I have news.**
> 
> 
> Your notes have more power now.
> 
> And your Gallery learned how to organize itself.
> 

---

### X3 — Search

Now users have had time to accumulate:

PINs + notes + assets.

So retrieval actually matters.

Ship **reliable Search**, not “AI search.”

This also gives IIS something valuable to observe:

- What users search
- Search success/failure without collecting private query content
- repeated searches
- which Surface objects users retrieve most
- time to retrieval

Later intelligence can grow from actual retrieval behavior.

---

### X4 — Widgets

First widget generation.

Keep it basic:

- New PIN
- Camera
- Notes
- Gallery
- Search if appropriate

Small/medium configurations.

The job is simply:

> **Surface without opening Surface.**
> 

---

### X5 — Widgets grow up

Now widgets become configurable and substantially better:

- Choose actions
- Duo configurations
- Four-action configurations
- Larger Surface Command widget
- Search entry
- potentially useful PIN/follow-up information if research supports it

So X4 establishes widgets.

**X5 makes widgets Surface-quality.**

That distinction works.

---

### X6 — Follow-up grows up

This is also a clean progression.

X1:

> `Hello [name] garu, ala unnaru?`
> 

One Surface-owned framework.

X6:

User can edit the **global framework**:

> `[name] garu, ala unnaru?`
> 

or

> `Hello [name], how are you?`
> 

or whatever they prefer.

Every automated/prepared initiation uses that framework.

Don't immediately add per-person templates.

Later, if IIS shows users repeatedly wanting different communication styles:

```
Default framework
Customer framework
Business prospect framework
Existing distributor framework
Individual framework
```

That capability gets **earned by evidence**.

---

### X7 — Productivity

And this one should deliberately remain:

> **TBD — IIS driven**
> 

Don't decide today that X7 needs tasks, calendars, streaks, pipelines, AI prioritization, goals, or dashboards.

By X7 you should have months of:

- follow-up behavior
- PIN creation patterns
- Gallery usage
- Notes behavior
- search failures
- widget usage
- retention
- feature requests
- support reports
- subscription behavior

Then IIS asks:

> **What repeatedly prevents Surface users from completing their work?**
> 

That's where X7 comes from.

That's genuine product development rather than founder imagination.

## Build & Iteration

Surface X1 was implemented as a functional Android prototype rather than only a design prototype. Development was intentionally incremental: establish the interface, audit what was actually functional, build the local data foundation, and then complete the core workflows required for real-world testing.

### Initial Implementation

The first implementation reproduced much of the intended Surface interface, but an implementation audit revealed that most of the product was still static.

Gallery, Notes, Camera, PINs, and New PIN existed as navigation destinations but opened placeholder screens. Home contained hardcoded visual representations rather than actual user data.

This created an important distinction between **visual completion and product completion**. The application looked partially built, but the core user loops did not yet exist.

### Data Foundation

Before adding more UI, I prioritized a local data foundation for X1.

A Room database was introduced for:

- Gallery assets
- Notes
- PINs
- Follow-ups

Gallery stores references to local images rather than image blobs. Repository layers expose the data reactively to the interface, allowing changes made within the application to update relevant surfaces such as Home.

X1 was deliberately kept local-first without introducing a backend or cloud dependency before the core workflow had been validated.

### Functional Implementation

The next iterations converted the major placeholders into working product loops.

**Gallery**

`Import image → persist → display → open → delete`

Imported images remain available after application restart, and recent Gallery content can appear on Home.

**Notes**

`Create note → write → autosave → reopen → edit → persist`

Notes are stored locally and remain available after restarting the application. The latest note can also be surfaced on Home.

**Camera**

`Open camera → capture image → save locally → add to Surface Gallery`

Camera capture and Gallery are therefore connected rather than operating as isolated features.

**PINs**

Recent PIN cards were made navigable so that selecting one leads to a PIN destination and supports normal back navigation.

### Implementation Issues

The functional implementation exposed several design-fidelity problems.

The current Notes interface does not yet match the intended Notes design. The Camera is functional but does not follow the designed interface or the intended Home-tile expansion/collapse transition. The bottom navigation still has visual inconsistencies and an incorrect Notes routing behavior. Home retains some alignment and proportion differences from the reference design, and the menu icon does not match the intended design.

The intended Open Sauce typography was also found to be absent from the Android project resources, meaning the current build uses the Android system sans-serif fallback.

These issues were documented rather than delaying field testing for visual perfection.

### Current X1 State

At the end of this development cycle, Surface has working local persistence and usable core loops for Gallery, Notes, Camera, and basic PIN navigation.

The decision was made to **stop adding features and move the current build into real invitation work**.

The purpose of the next stage is not to determine whether the interface is visually finished, but to observe whether Surface actually improves the workflow it was designed for.

---

## User Testing & Learnings

Surface X1 will be used during real invitation work rather than tested only through predefined prototype tasks.

Testing will involve both my own usage and usage by an existing network marketer during normal work.

The evaluation will focus on:

- Which Surface features are naturally used without prompting
- Where users hesitate or become confused
- Tasks that still require leaving Surface for another application
- Unnecessary steps or navigation
- Missing information during prospect interactions
- Features that appeared important during planning but receive little real usage
- Reliability problems such as crashes, lost information, slow interactions, or incorrect navigation
- Workflows that prove noticeably more convenient than the existing process

Observations will be recorded as evidence rather than immediately converted into features.

| Observation | Evidence | Product Decision |
| --- | --- | --- |
| To be recorded during field use | — | — |
| To be recorded during field use | — | — |
| To be recorded during field use | — | — |
| To be recorded during field use | — | — |
| To be recorded during field use | — | — |

After the field-testing period, these observations will determine the priorities for the next Surface iteration and whether the original product hypothesis is supported by actual usage.
