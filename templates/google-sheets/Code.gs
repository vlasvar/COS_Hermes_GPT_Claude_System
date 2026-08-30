/**
 * Chief of Staff System — Google Sheets provisioner.
 * @OnlyCurrentDoc
 *
 * Usage:
 * 1. Create a blank Google Sheet.
 * 2. Open Extensions → Apps Script.
 * 3. Paste this file into Code.gs.
 * 4. Run provisionChiefOfStaffSystem and authorize access to this Sheet.
 *
 * The script creates generic tabs and headers only. It does not collect,
 * transmit, or seed personal data.
 */
function provisionChiefOfStaffSystem() {
  const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  const schema = getChiefOfStaffSchema_();

  schema.forEach(definition => {
    let sheet = spreadsheet.getSheetByName(definition.name);
    if (!sheet) sheet = spreadsheet.insertSheet(definition.name);

    if (sheet.getMaxColumns() < definition.columns.length) {
      sheet.insertColumnsAfter(
        sheet.getMaxColumns(),
        definition.columns.length - sheet.getMaxColumns()
      );
    }

    const existingHeaders = sheet
      .getRange(1, 1, 1, definition.columns.length)
      .getValues()[0];
    const isBlank = existingHeaders.every(value => value === '');
    const matchesSchema = definition.columns.every(
      (column, index) => existingHeaders[index] === column
    );

    if (!isBlank && !matchesSchema) {
      throw new Error(
        `Tab "${definition.name}" already exists with different headers. ` +
        'No data was changed.'
      );
    }

    sheet.getRange(1, 1, 1, definition.columns.length)
      .setValues([definition.columns])
      .setFontWeight('bold')
      .setBackground('#E8EEF9');
    sheet.setFrozenRows(1);
    sheet.autoResizeColumns(1, definition.columns.length);
    if (!sheet.getFilter()) {
      sheet
        .getRange(1, 1, Math.max(sheet.getMaxRows(), 2), definition.columns.length)
        .createFilter();
    }
  });

  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('Inbox'));
  SpreadsheetApp.flush();
}

function getChiefOfStaffSchema_() {
  return [
    {name: 'Inbox', columns: ['Inbox ID','Received At','Source','Summary','Status','Proposed Destination','Evidence Link','Processed At']},
    {name: 'Projects', columns: ['Project ID','Name','Desired Outcome','Owner','Status','Review Date','Next Action ID','Evidence Link','Updated At']},
    {name: 'Actions', columns: ['Action ID','Project ID','Action','Owner','Due Date','Status','Approval State','Evidence Link','Updated At']},
    {name: 'Commitments', columns: ['Commitment ID','Direction','Party','Commitment','Made At','Due Date','Status','Evidence Link','Updated At']},
    {name: 'Decisions', columns: ['Decision ID','Question','Decision','Rationale','Decided At','Revisit Trigger','Evidence Link','Updated At']},
    {name: 'Contacts', columns: ['Contact ID','Display Name','Type','Context','Status','Last Interaction','Evidence Link','Updated At']},
    {name: 'Reviews', columns: ['Review ID','Period Start','Period End','Summary','Risks','Priorities','Created At','Evidence Link']},
    {name: 'Agent Log', columns: ['Log ID','Timestamp','Agent','Operation','Target Type','Target ID','Approval State','Result','Evidence Link']}
  ];
}
